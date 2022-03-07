from django.utils import timezone
from uuid import uuid4
from django.db import models

# Create your models here.

class Question(models.Model):
    QUESTION_CATEGORIES = [
        ('HI', 'history'),
        ('SC', 'science'), 
        ('SP', 'sports'),
        ('AR','art'),
        ('GE', 'geography'),
        ('EN', 'entertaiment'), 
        ('NC', 'no category')
    ]
    id = models.UUIDField(primary_key=True, unique=True ,default=uuid4)
    text_question = models.CharField(max_length=255)
    category = models.CharField(max_length=2, choices=QUESTION_CATEGORIES)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_question


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, unique=True ,default=uuid4)
    text_answer = models.CharField(max_length=150, blank=False)
    correct_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)