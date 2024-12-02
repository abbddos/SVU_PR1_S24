"""
URL configuration for PR1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static 
from login import views as login_views
from admin_ import views as admin_views
from home_ import views as home_views
from services import views as services_views
from beneficiaries import views as beneficiaries_views 
from activities import views as activities_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('home/', include('home_.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'login/login.html'), name = 'login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'login/reset_password.html'), name = 'reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'login/password_reset_sent.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'login/password_reset_form.html'), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'login/password_reset_done.html'), name = 'password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login/logout.html'), name = 'logout'), 
    path('admin_/', include('admin_.urls')),
    path('activities/', include('activities.urls')),
    path('beneficiaries/', include('beneficiaries.urls')),
    path('services/', include('services.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
