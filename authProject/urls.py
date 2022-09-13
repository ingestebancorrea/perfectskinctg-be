from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
path('admin', admin.site.urls),
path('login/', TokenObtainPairView.as_view()),
path('refresh/', TokenRefreshView.as_view()),
path('user/', views.UserCreateView.as_view()),
path('user/<int:pk>/', views.UserDetailView.as_view()),
path('user/modified/<int:pk>', views.UserModifiedView.as_view()),
path('user/delete/', views.UserDeleteView.as_view()),
path('cliente/', views.ClienteCreateView.as_view()),
path('cliente/<int:pk>/', views.ClienteDetailView.as_view()),
]