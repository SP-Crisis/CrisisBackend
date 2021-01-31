from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name="Home"),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('search/', views.search, name="Search"),
    path("rank/", views.rank, name="Ranking"),
]