from rest_framework.generics import (CreateAPIView,ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView)

from .models import Todolist

from .serializers import TodolistSerializer

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

class TodolistListAPIView(ListAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()

class TodolistCreateApiView(CreateAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()

    
class TodolistListAPIView(ListAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()

    
class TodolistRetrieveAPIView(RetrieveAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()


class TodolistUpdateAPIView(UpdateAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()


class TodolistDestroyAPIView(DestroyAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()



#Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer