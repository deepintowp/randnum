from django.urls import path
from .views import GenerateNumView
urlpatterns = [
   
    path('randnum/', GenerateNumView.as_view(), name="randnum" ),
]
