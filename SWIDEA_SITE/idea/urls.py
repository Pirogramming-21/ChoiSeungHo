from django.urls import path
from .views import *

app_name = 'idea'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('change-interest/', change_interest, name='change_interest'),

]
