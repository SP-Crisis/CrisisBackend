from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answers
from .serializers import QuestionSerializer

from rest_framework import viewsets

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    