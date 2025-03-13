from django.urls import path
from .views import Urlgenerate  # Ensure this matches your view

urlpatterns = [
    path('', Urlgenerate.as_view(), name='home'),  # Root URL
]