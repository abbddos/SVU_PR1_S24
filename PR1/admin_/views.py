from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer


#API Views...


@api_view(['GET'])
def GetAllUsers(request):
    prf = Profile.objects.all().order_by('user__id')
    serializer = ProfileSerializer(prf, many = True)
    return Response(serializer.data)



@api_view(['GET'])
def GetUserByID(response, uid):
    try:
        prf = Profile.objects.get(user__username = uid)
    except Profile.DoesNotExist:
        return Response(status = 404)

    serializer = ProfileSerializer(prf, many = False)
    return Response(serializer.data, status=201)


@api_view(['POST'])
def CreateUser(request):
    serializer = ProfileSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status = 400)


@api_view(['PUT'])
def UpdateUser(request, uid):
    try:
        prf = Profile.objects.get(user__username = uid)
    except Profile.DoesNotExist:
        return Response(status = 404)

    serializer = ProfileSerializer(prf, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(seralizer.errors, status = 400)

 
@api_view(['DELETE'])
def DeleteUser(request, uid):
    try:
        prf = Profile.objects.get(user__username = uid)
    except Profile.DoesNotExist:
        return Response(status = 404)
    
    prf.delete()
    return Response(status = 201)        

