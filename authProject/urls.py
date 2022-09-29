from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'cita', views.CitaView, basename='cita')
router.register(r'empleado', views.EmpleadoView, basename='empleado')

urlpatterns = [
path('admin', admin.site.urls),
path('login/', TokenObtainPairView.as_view()),
path('refresh/', TokenRefreshView.as_view()),
path('user/', views.UserCreateView.as_view()),
path('user/<int:pk>/', views.UserDetailView.as_view()),
path('categoria/', views.CategoriaCreateView.as_view()),
path('categoria/<int:pk>/', views.CategoriaDetailView.as_view()),
]

urlpatterns += router.urls