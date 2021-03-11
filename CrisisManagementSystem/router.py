from backend.views import QuestionViewSet, AnswerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet)

urlpatterns = router.urls