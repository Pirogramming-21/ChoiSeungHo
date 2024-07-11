from django.urls import path
from .views import *

urlpatterns = [
    path('add/', review_add, name='review_add')
]