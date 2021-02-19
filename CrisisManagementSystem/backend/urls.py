from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [ 
    path('', views.index),
    path('list/', views.list),
    path('question-detail/<str:pk>/', views.detail),
    path('question-create/', views.create)
]
=======
urlpatterns = [
    path('', views.index, name="Home"),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('questions/<int:question_id>/', views.questions, name="QList"),
    path('questions/', views.allQuestions, name="All Questions"),
    path('search/', views.search, name="Search"),
    path("rank/", views.rank, name="Ranking"),
    path("policies/", views.policies, name="Policies"),
]
>>>>>>> be-PoliciesModel
