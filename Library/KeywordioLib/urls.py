"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Home/', views.Home, name='Home'),
    path('signup/', views.signup, name='signup'),
    path('loginsignup/', views.loginsignup, name='loginsignup'),
    path('loginsignup/Admin', views.Admin, name='admin1'),
    path('loginsignup/StudentView', views.loginsignup, name='StudentView'),
    path('loginsignup/Admin/create', views.create, name='create'),
    path('loginsignup/Admin/read', views.read, name='read'),
    path('loginsignup/Admin/update', views.update, name='update'),
    path('loginsignup/Admin/delete', views.delete, name='delete'),
    
]