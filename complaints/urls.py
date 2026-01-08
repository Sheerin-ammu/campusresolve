from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
]
