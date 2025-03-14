from django.urls import path
from .views import LinkGenerator, URLListView  

urlpatterns = [
    path('', LinkGenerator.as_view(), name='home'),
    path('urls/', URLListView.as_view(), name='url_list'),  ]