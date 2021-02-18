from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answers
from .serializers import QuestionSerializer
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Just a placeholder for how I think these views would work. Need to convert to the other style of views (@api_view)
class RegisterView(FormView):

    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'register.html', content)

    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect(reverse('dashboard-view'))
        content['form'] = form
        template = 'register.html'
        return render(request, template, content)

#There is no Dashboard view yet, I'm not sure how we're going to do it, but I still put dashboard for the redirect
class LoginView(FormView):

    content = {}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            return redirect(reverse('dashboard-view'))
        content['form'] = LoginForm
        return render(request, 'login.html', content)

    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username=users.first().username, password=password)
            login(request, user)
            return redirect(reverse('dashboard-view'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Invalid user credentials' + e
            return render_to_response('login.html', content)
