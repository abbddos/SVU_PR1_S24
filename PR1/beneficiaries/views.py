from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Beneficiary
from .serializers import BeneficiarySerializer
from django.http import FileResponse
import pandas as pd


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
def CreateBeneficiary(request):
    serializer = BeneficiarySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['PUT'])
def UpdateBeneficiary(request, bid):
    try:
        bn = Beneficiary.objects.get(beneficiary_id = bid)
    except Beneficiary.DoesNotExist:
        return Response(status=404)

    serializer = BeneficiarySerializer(bn, data = request.data)
    if serializer.is_valid():
        seralizer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def DeleteBeneficiary(request, bid):
    try:
        bn = Beneficiary.objects.get(beneficiary_id = bid)
    except Beneficiary.DoesNotExist:
        return Response(status=404) 

    bn.delete()
    return Response(status=201)
