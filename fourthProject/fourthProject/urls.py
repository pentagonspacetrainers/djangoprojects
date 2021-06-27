"""fourthProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from BangaloreApp import views as b
from MysoreApp import views as m
from HassanApp import views as h

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bangalore/vijayanagar/',b.corona_vijayanagar),
    path('bangalore/jayanagar/',b.corona_jayanagar),\
    path('bangalore/rajajinagar/',b.corona_rajajinagar),


    path('mysore/vijayanagar',m.corona_vijayanagar),
    path('mysore/kdroad',m.corona_kdroad),
    path('mysore/rknagar',m.corona_rknagar),

    path('hassan/satyamangala',h.corona_satyamangala),
    path('hassan/crpatna',h.corona_crpatna),
    path('hassan/arsikere',h.corona_arsikere),

]

