from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Question(models.Model):
    date = models.DateTimeField('Date Asked')
    rank = models.IntegerField(default=0)
    question = models.CharField(max_length=500)
    def __str__(self):
        return self.question

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    rank = models.IntegerField(default=0)
    def __str__(self):
        return self.answer

class Policies(models.Model):
    levels = models.TextChoices('Level', 'SCHOOL STATE FEDERAL')
    policy = models.CharField(max_length=500)
    date = models.DateTimeField('Last Updated')
    level = models.CharField(blank=True,
    options = levels.choices, max_length=10)
     def __str__(self):
        return self.policy

class Technologies(models.Model):
    types = models.TextChoices('Type', 'COVID CAMPUS')
    technology = models.CharField(max_length=500)
    type = models.CharField(blank=True,
    options = types.choices, max_length=10)
     def __str__(self):
        return self.technology

class Operations(models.Model):
    operation = models.CharField(max_length=500)
    def __str__(self):
        return self.operation

#Health: about COVID virus, the pandemic, symptom, and possible countermeasures (e.g., vaccines), available health sources?
#(May need to add to model)

class Health(models.Model):
    information = models.CharField(max_length=500)
    def __str__(self):
        return self.information
