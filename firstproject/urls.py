"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

admin.site.site_header = "Aman jha registration page"
admin.site.site_title = "tile "
admin.site.index_title = "Welcome to our page"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.reg),
    path('success',views.suc,name="success"),
    path('qoute',views.qoute),
    path('home',views.hom),
    path('homesuc',views.homsuc),
    path('all',views.all)
]
