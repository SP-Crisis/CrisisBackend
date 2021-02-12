from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
    path('', views.index),
    path('list/', views.list),
    path('question-detail/<str:pk>/', views.detail),
    path('question-create/', views.create)
]
