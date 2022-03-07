from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer = UserSerializer