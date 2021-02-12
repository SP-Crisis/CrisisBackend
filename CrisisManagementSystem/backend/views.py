from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answers
from .serializers import QuestionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


<<<<<<< HEAD
@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/list/',
        'Detail': '/question-detail/<str:pk>/',
        'Create': '/question-create/',
        'Update': '/question-update/<str:pk>/',
        'Delete': '/question-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def list(request):
=======
def dashboard(request):
    return HttpResponse("Dashboard")

def allQuestions(request):
>>>>>>> be-PoliciesModel
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)

<<<<<<< HEAD
=======
def questions(request, question_id):
    question = Question.objects.get(pk=question_id)

    return HttpResponse(question.question)
>>>>>>> be-PoliciesModel

@api_view(['POST'])
def create(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

<<<<<<< HEAD
=======
def rank(request):
    return HttpResponse("Ranking Here")

def policies(request):
    return HttpResponse("Policies")
>>>>>>> be-PoliciesModel
