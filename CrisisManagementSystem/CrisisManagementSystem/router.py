from backend.views import QuestionViewSet, AnswerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionViewSet, basename='question')
router.register('answers', AnswerViewSet, basename="answer")

