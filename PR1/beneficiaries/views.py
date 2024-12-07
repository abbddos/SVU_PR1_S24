from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import Beneficiary
from .serializers import BeneficiarySerializer
from .forms import BeneficiaryForm
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd
import pyqrcode
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
import os
from xhtml2pdf import pisa
from django.http import HttpResponse


@login_required
def Beneficiaries(request):
    return render(request, 'beneficiaries/beneficiaries_register.html',{'form': BeneficiaryForm})

@login_required
def PrintID(request, bid):
    try:
        bn = Beneficiary.objects.get(beneficiary_id = bid)
    except Beneficiary.DoesNotExist:
        return False 
    return render(request, 'beneficiaries/beneficiary_id.html', {'ben': bn})



# API Views


@api_view(['GET'])
def GetAllBeneficiaries(request):
    bn = Beneficiary.objects.all().order_by('beneficiary_id')
    serializer = BeneficiarySerializer(bn, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def GetBeneficiaryByID(request, bid):
    try:
        bn = Beneficiary.objects.get(beneficiary_id = bid)
    except Beneficiary.DoesNotExist:
        return Response(status=404)
    
    serializer = BeneficiarySerializer(bn, many = False)
    return Response(serializer.data, status=201)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def CreateBeneficiary(request, format = None):
    data_ = request.data.copy() 
    ben_name = f"{data_['first_name']}_{data_['middle_name']}_{data_['last_name']}" 
    serializer = BeneficiarySerializer(data = data_)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def UpdateBeneficiary(request, bid):
    try:
        bn = Beneficiary.objects.get(beneficiary_id = bid)
    except Beneficiary.DoesNotExist:
        return Response(status=404)

    serializer = BeneficiarySerializer(bn, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def DeleteBeneficiary(request, bid):
    try:
        bn = Beneficiary.objects.get(beneficiary_id = bid)
    except Beneficiary.DoesNotExist:
        return Response(status=404) 

    bn.delete()
    return redirect('beneficiaries_register')
