from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Question, Answers

# Register your models here.
admin.site.register(Question)
admin.site.register(Answers)

#New Comment
