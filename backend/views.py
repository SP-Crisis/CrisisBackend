from .models import Question, Answers
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password

from .serializers import QuestionSerializer, AnswerSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions

from rest_framework_simplejwt.tokens import RefreshToken


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer
