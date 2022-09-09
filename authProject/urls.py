from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
path('login/', TokenObtainPairView.as_view()),
path('refresh/', TokenRefreshView.as_view()),
path('cliente/', views.ClienteCreateView.as_view()),
path('cliente/<int:pk>/', views.ClienteDetailView.as_view()),
]