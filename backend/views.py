from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answers
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password

from .serializers import QuestionSerializer, AnswerSerializer

from rest_framework import viewsets

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer
