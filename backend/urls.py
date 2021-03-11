from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index),
    path('list/', views.list),
    path('question-detail/<str:pk>/', views.detail),
    path('question-create/', views.create),
]
    ##path('register/', RegisterView.as_view(), name='register-view'),
    ##ath('login/', LoginView.as_view(), name='login-view'),