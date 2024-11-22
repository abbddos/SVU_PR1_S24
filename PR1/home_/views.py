from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from admin_.models import Profile

@login_required()
def home(request):
    prf = Profile.objects.get(email = request.user.email)
    context = {'prf' : prf}
    return render(request, 'home_/home.html', context)