from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("Main Login")

def dashboard(request):
    return HttpResponse("Dashboard")

def allQuestions(request):
    questions = Question.objects.all()
    return HttpResponse(questions)

def questions(request, question_id):
    question = Question.objects.get(pk=question_id)

    return HttpResponse(question.question)

def search(request):
    return HttpResponse("Search")

def rank(request):
    return HttpResponse("Ranking Here")

def policies(request):
    return HttpResponse("Policies")
