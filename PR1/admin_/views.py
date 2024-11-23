from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile
from .forms import UserRegisterForm, UserProfileForm
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, UpdateProfileSerializer

@login_required
def UserProfile(request, uid):
    form = UserProfileForm()
    context = {
        'form': form
    }
    return render(request, "admin_/profile.html", context)

@login_required
def ChangePassword(request, uid):
    prf = Profile.objects.get(email = request.user.email)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            try:
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Please correct the error above.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'admin_/change_password.html', context)


#API Views...

@api_view(['GET'])
def GetAllUsers(request):
    prf = Profile.objects.all().order_by('user__id')
    serializer = ProfileSerializer(prf, many = True)
    return Response(serializer.data)



@api_view(['GET'])
def GetUserByID(response, uid):
    try:
        prf = Profile.objects.get(email = uid)
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


@api_view(['POST'])
def UpdateUser(request, uid):
    try:
        prf = Profile.objects.get(email = uid)
    except Profile.DoesNotExist:
        return Response(status = 404)

    serializer = UpdateProfileSerializer(prf, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status = 400)

 
@api_view(['POST'])
def DeleteUser(request, uid):
    try:
        prf = Profile.objects.get(email = uid)
    except Profile.DoesNotExist:
        return Response(status = 404)
    
    prf.delete()
    return Response(status = 201)        

