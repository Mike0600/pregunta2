#Rest
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView

#Local
from .serializers import AnswerSerializer, QuestionSerializer, QuestionarySerializer
from .models import AnswerUser, QuestionUser, QuestionaryUser
from users import serializers

import uuid



class QuestionaryViewSet(viewsets.ModelViewSet):
    queryset = QuestionaryUser.objects.all()
    serializer_class = QuestionarySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, pk=None):
        user_info = serializers.UserSerializerResponse(request.user).data
        data = {
            'name': request.data['name'],
            'created_by' : user_info['id'],
            'is_public' : request.data['is_public'],
        }

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        return Response({'status': 'Bad Request',
                         'message': serializer.is_valid()},
                          status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, pk=None):
        user_info = serializers.UserSerializerResponse(request.user).data
        queryset = QuestionaryUser.objects.filter(created_by=user_info['id'])
        serializer = QuestionarySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        user_info = serializers.UserSerializerResponse(request.user).data
        question = QuestionaryUser.objects.get(id=request.data['id'])
        print(type(QuestionarySerializer(question).data['created_by']))
        print(type(user_info['id']))
        if str(QuestionarySerializer(question).data['created_by']) == user_info['id']:
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionUser.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, pk=None):
        data = {
            'questionary': request.data['questionary'],
            'text_question' : request.data['text_question'],
        }

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        return Response({'status': 'Bad Request',
                         'message': serializer.is_valid()},
                          status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getQuestionary(request):
    query = QuestionUser.objects.filter(questionary=request.data['questionary'])
    return Response(query.values())

@api_view(['GET', 'PUT'])
def getQuestion(request):
    if request.method == 'GET':
        queryQuestion = QuestionUser.objects.get(id=request.data['id'])
        queryAnswers = AnswerUser.objects.filter(question=queryQuestion.id)
        if queryQuestion:
            data = {
                'question' : QuestionSerializer(queryQuestion).data,
                'answers' : queryAnswers.values()
            }
            return Response(data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #elif request.method == 'PUT':





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
        