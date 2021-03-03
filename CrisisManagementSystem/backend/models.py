from django.db import models
import datetime

# Create your models here.

class Question(models.Model):
    rank = models.IntegerField(default=0)
    question = models.CharField(max_length=500)
    def __str__(self):
        return self.question

class Answers(models.Model):
    answer = models.CharField(max_length=500)
    rank = models.IntegerField(default=0)
    def __str__(self):
        return self.answer

class Policies(models.Model):
    level = models.CharField(max_length=10)
    policy = models.CharField(max_length=500)
    date = models.DateTimeField('Last Updated')
    def __str__(self):
        return self.policy

class Technologies(models.Model):
    types = models.CharField(max_length=10)
    technology = models.CharField(max_length=500)
    def __str__(self):
        return self.technology

class Operations(models.Model):
    date = models.DateTimeField('Hours of Operation')
    operation = models.CharField(max_length=500)
    def __str__(self):
        return self.operation

#Health: about COVID virus, the pandemic, symptom, and possible countermeasures (e.g., vaccines), available health sources?
#(May need to add to model)

class Health(models.Model):
    information = models.CharField(max_length=500)
    def __str__(self):
        return self.information
