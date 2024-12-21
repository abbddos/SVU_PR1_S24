from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer
from .forms import ActivityForm
from django.http import FileResponse
from beneficiaries.models import Beneficiary
import pandas as pd

@login_required
def RegisterActivity(request):
    return render(request, 'activities/register_activity.html', {'form': ActivityForm})

@login_required
def ViewHistory(request, bid):
    bn = Beneficiary.objects.get(beneficiary_id = bid)
    ac = Activity.objects.filter(beneficiary = bn)
    services = set(activity.service for activity in ac)
    return render(request, 'activities/history.html', {'ben': bn, 'ser': services})

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


@api_view(['PUT'])
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


@api_view(['DELETE'])
def DeleteActivity(request, aid):
    try:
        ac = Activity.objects.get(activity_id = aid)
    except Activity.DoesNotExist:
        return Response(status=404) 

    ac.delete()
    return Response(status=201)
