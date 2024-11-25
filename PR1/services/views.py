from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer
from .forms import ServiceForm
from django.http import FileResponse
import pandas as pd

# Web Views...

@login_required 
def Services(request):
    return render(request, 'services/services.html', {'form': ServiceForm()})


# API Views

@api_view(['GET'])
def GetAllServices(request):
    sr = Service.objects.all().order_by('service_id')
    serializer = ServiceSerializer(sr, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def GetServiceByID(request, sid):
    try:
        sr = Service.objects.get(service_id = sid)
    except Service.DoesNotExist:
        return Response(status=404)
    
    serializer = ServiceSerializer(sr, many = False)
    return Response(serializer.data, status=201)


@api_view(['POST'])
def CreateService(request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def UpdateService(request, sid):
    try:
        sr = Service.objects.get(service_id = sid)
    except Service.DoesNotExist:
        return Response(status=404)

    serializer = ServiceSerializer(sr, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['Get'])
def DeleteService(request, sid):
    try:
        sr = Service.objects.get(service_id = sid)
    except Service.DoesNotExist:
        return Response(status=404) 

    sr.delete()
    return redirect('all_services')