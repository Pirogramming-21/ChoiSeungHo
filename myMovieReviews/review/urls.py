from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('add/', review_add, name='review_add'),
    path('review/<int:pk>', review_detail, name='review_detail'),
    path('review/<int:pk>/update', review_update, name='review_update'),
    path('review/<int:pk>/delete', review_delete, name='review_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
