from django.urls import path
from .views import sendData, BrakeDataListView

urlpatterns = [
  path('send/', sendData),
  path('percent/', BrakeDataListView.as_view()),
]