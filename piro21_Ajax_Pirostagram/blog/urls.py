from django.urls import path
from .views import *

app_name = 'posts'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/update', post_update, name='post_update'),
    path('<int:pk>/delete', post_delete, name='post_delete'),
    path('<int:pk>/comments/create', comment_create, name='comment_create'),
    path('<int:pk>/comments/delete', comment_delete, name='comment_delete'),
    path('like/', like, name='like'),
    path('comment/', comment, name='comment'),
    path('delete_comment/<int:pk>/', comment_delete, name='comment_delete'),

]
