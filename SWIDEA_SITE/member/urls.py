# urls.py
from django.urls import path
from .views import *

app_name = 'member'

urlpatterns = [

    path('create', create, name='create'),
]
