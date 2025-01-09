from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer
from .forms import ActivityForm, EventForm
from django.http import FileResponse
from beneficiaries.models import Beneficiary
import pandas as pd
import requests
from io import BytesIO
from datetime import datetime


def GetFourWsData(start_date, end_date):
    response = requests.get("http://127.0.0.1:8000/activities/GetAllActivities/")
    response.raise_for_status()
    if response.headers['Content-Type'] == 'application/json':
        data = response.json()
        df = pd.json_normalize(data)
        df['service.start_date'] = pd.to_datetime(df['service.start_date']).dt.date
        df['service.end_date'] = pd.to_datetime(df['service.end_date']).dt.date

        df = df[df['service.start_date'] >= start_date]
        df = df[df['service.end_date'] <= end_date]

        grouped_df = df.groupby(['service.service_type','service.start_date', 'service.end_date','service.governorate', 'service.district', 'service.sub_district','service.village_neighborhood']).agg(
                            Total_individuals = ('beneficiary.householod_size', 'sum'),
                            Males=('beneficiary.sex', pd.NamedAgg(column='beneficiary.sex', aggfunc=lambda x: len(x[x == 'Male']))),
                            Females=('beneficiary.sex', pd.NamedAgg(column='beneficiary.sex', aggfunc=lambda x: len(x[x == 'Female']))),
                            Disabilities=('beneficiary.disability_in_household', pd.NamedAgg(column='beneficiary.disability_in_household', aggfunc=lambda x: len(x[x == 'Yes']))),
                            Infants=('beneficiary.infants_in_household', pd.NamedAgg(column='beneficiary.infants_in_household', aggfunc=lambda x: len(x[x == 'Yes']))),
                            Elders=('beneficiary.elders_in_household', pd.NamedAgg(column='beneficiary.elders_in_household', aggfunc=lambda x: len(x[x == 'Yes'])))
                    )

    return grouped_df


@login_required
def RegisterActivity(request):
    return render(request, 'activities/register_activity.html', {'form': ActivityForm})

@login_required
def ViewHistory(request, bid):
    bn = Beneficiary.objects.get(beneficiary_id = bid)
    ac = Activity.objects.filter(beneficiary = bn)
    services = set(activity.service for activity in ac)
    return render(request, 'activities/history.html', {'ben': bn, 'ser': services})

@login_required
def Reports(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            report_type = form.cleaned_data['report_type']
            if report_type == '4Ws':
                df = GetFourWsData(start_date, end_date)
                buffer = BytesIO()
                df.to_excel(buffer, index=True)
                filename = 'four_ws_data.xlsx'
                response = HttpResponse(
                    buffer.getvalue(), 
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response  
            elif report_type == 'Infographic':
                return redirect('infographic-report')
            
    else:
        form = EventForm()
    return render(request, 'activities/reports.html', {'form': form})


@login_required
def InfogragphicReport(request):
    return render(request, 'activities/infographic_report.html')




# API Views


@api_view(['GET'])
def GetAllActivities(request):
    ac = Activity.objects.all().order_by('activity_id')
    serializer = ActivitySerializer(ac, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def GetActivityByID(request, aid):
    try:
        ac = Activity.objects.get(activity_id = aid)
    except Activity.DoesNotExist:
        return Response(status=404)
    
    serializer = ActivitySerializer(ac, many = False)
    return Response(serializer.data, status=201)


@api_view(['POST'])
def CreateActivity(request):
    serializer = ActivitySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def UpdateActivity(request, aid):
    try:
        ac = Activity.objects.get(activity_id = aid)
    except Activity.DoesNotExist:
        return Response(status=404)

    serializer = ActivitySerializer(ac, data = request.data)
    if serializer.is_valid():
        seralizer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def DeleteActivity(request, aid):
    try:
        ac = Activity.objects.get(activity_id = aid)
    except Activity.DoesNotExist:
        return Response(status=404) 

    ac.delete()
    return redirect('reports')
