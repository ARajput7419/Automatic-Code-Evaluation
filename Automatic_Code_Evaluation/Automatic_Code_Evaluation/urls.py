"""Automatic_Code_Evaluation URL Configuration

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
from Automatic_Code_Evaluation import home
from Automatic_Code_Evaluation.evaluate import evaluator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit_code/', evaluator.code_submit),
    path('evaluator', evaluator.executor),
    path('contact/', evaluator.contact),
    path('', home.index),
    path('evaluate',evaluator.executor),
    path('testing/',evaluator.form)
]
