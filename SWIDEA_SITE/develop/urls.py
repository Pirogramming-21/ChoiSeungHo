from django.urls import path
from .views import *

app_name = 'develop'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),

]
