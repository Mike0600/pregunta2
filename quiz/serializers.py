#Rest
from rest_framework import serializers

#Local
from .models import QuestionaryUser, AnswerUser, QuestionUser


class QuestionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionaryUser
        fields = '__all__'



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionUser
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerUser
        fields = '__all__'



