from django.db import models

# Create your models here.
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
