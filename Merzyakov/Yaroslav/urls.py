from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductAPIView.as_view()),
    path('<int:pk>/', views.ProductAPIView.as_view()),

]
