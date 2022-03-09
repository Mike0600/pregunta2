#Rest
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

#Local
from .serializers import AnswerSerializer, QuestionSerializer, QuestionarySerializer
from .models import AnswerUser, QuestionUser, QuestionaryUser


class QuestionaryViewSet(viewsets.ModelViewSet):
    queryset = QuestionaryUser.objects.all()
    serializer_class = QuestionarySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionUser.objects.all()
    serializer_class = QuestionSerializer
    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = AnswerUser.objects.all()
    serializer_class = AnswerSerializer


class GetRandomQuestion(APIView):
    def get(self, request, format=None):
        q_category = request.GET['questionary']
        questionary = QuestionaryUser.objects.get(name=q_category)
        random_question = QuestionUser.objects.filter(questionary=questionary.id).order_by('created_date').first()
        answers = AnswerUser.objects.filter(question_id=random_question.id)
        data = {
            'questionary': QuestionarySerializer(questionary).data,
            'question' : QuestionSerializer(random_question).data,
            'answers' : answers.values(),
        }
        return Response(data)
        