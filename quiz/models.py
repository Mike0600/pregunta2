#Utils
from uuid import uuid4

#Django
from django.db import models
from users.models import User


class QuestionaryUser(models.Model):
    id = models.UUIDField(primary_key=True, unique=True ,default=uuid4)
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class QuestionUser(models.Model):
    id = models.UUIDField(primary_key=True, unique=True ,default=uuid4)
    questionary = models.ForeignKey(QuestionaryUser, on_delete=models.CASCADE)
    text_question = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text_question


class AnswerUser(models.Model):
    id = models.UUIDField(primary_key=True, unique=True ,default=uuid4)
    text_answer = models.CharField(max_length=150, blank=False)
    correct_answer = models.BooleanField(default=False)
    question = models.ForeignKey(QuestionUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_answer

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
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text_question


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, unique=True ,default=uuid4)
    text_answer = models.CharField(max_length=150, blank=False)
    correct_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)