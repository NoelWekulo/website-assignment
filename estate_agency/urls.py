"""
URL configuration for estate_agency project.

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
from django.urls import path
from agency import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('/', views.index, name="index"),

    path('about/', views.about, name="about"),

    path('blog/', views.blog, name="blog"),
    path('singleblog/', views.singleblog, name="singleblog"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('agents/', views.agents, name="agents"),
    path('properties/', views.properties, name="properties"),
    path('propertySingle/', views.propertysingle, name="propertysingle"),
    path('servicedetails/', views.servicedetails, name="servicedetails"),
    path('starterpage/', views.starterpage, name="starterpage"),
    path('blogdetails/', views.blogdetails, name="blogdetails")
]
