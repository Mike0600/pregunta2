from unicodedata import category
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
        q_category = request.GET['category']
        if q_category == 'AN':
            random_question = Question.objects.order_by('?').first()
        else:
            random_question = Question.objects.filter(category=q_category).order_by('?').first()
        answers = Answer.objects.filter(question_id=random_question.id)
        data = {
            'question' : QuestionSerializer(random_question).data,
            'answers' : answers.values(),
        }
        return Response(data)
        