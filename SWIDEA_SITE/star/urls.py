from django.urls import path
from .views import *

app_name = 'star'

urlpatterns = [
    path('int<pk>/', push, name='push'),
    path('int<pk>/delete', delete, name='delete'),
]
