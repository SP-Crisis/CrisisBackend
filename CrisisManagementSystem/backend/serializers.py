from rest_framework import serializers
from .models import Question, Answers, Policies, Technologies, Operations, Health, User

#Serializers
## Main Serial

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policies
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = '__all__'

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = '__all__'

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#Django's user model has the following fields:
#username, first_name, last_name, email, password, groups,
#user_permissions, is_staff, is_active, is_superuser, last_login, date_joined
#We can discuss which fields to use, I just left it as all for now to test
