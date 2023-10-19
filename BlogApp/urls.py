from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('aboutpage/', views.about),
]
