"""poll URL Configuration

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
from django.contrib import admin
from django.urls import path
from pollapp import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.deom),
    path('signup',views.signupform),
    path('signupdata',views.singupdata),
    path('signin',views.signinform,name='signin'),
    path('signindata',views.signindata),
    path('logout',views.logoutdata),
    path('createform',views.createform),
    path('create',views.createdata),
    path('polls',views.polls_now),
    path('pollnswer',views.poll_vote),
    path('res',views.resultspage),
    path('result',views.results)
]

