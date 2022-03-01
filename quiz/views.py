from .models import Answer, Question
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnswerSerializer, QuestionSerializer

import uuid

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class GetRandomQuestion(APIView):
    def get(self, request, format=None):
        random_question = Question.objects.none()
        answers = Answer.objects.none()
        random_question = Question.objects.order_by('?')[:1:0]
        answers = Answer.objects.filter(question_id=random_question.values('id'))
        data = {
            'question' : random_question.values(),
            'answers' : answers.values(),
        }
        return Response(data)