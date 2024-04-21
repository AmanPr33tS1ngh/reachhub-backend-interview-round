from .views import IngestionAPI
from django.urls import path

urlpatterns = [
    path("", IngestionAPI.as_view(), name="")
]
