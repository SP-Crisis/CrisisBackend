from rest_framework import serializers
from .models import Question, Answers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Answers
        fields = '__all__'