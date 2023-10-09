from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import MyUser
from .serializers import MyUserSerializerGET, MyUserSerializerPOST
# Create your views here.

class ApiGetUserView(APIView):

    def get(self, request, format = None, users = None):
        users = MyUser.objects.all()
        users_serializer = MyUserSerializerGET(users, many = True)

        if users:
            return Response(users_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Users not found"}, status=status.HTTP_404_NOT_FOUND)
        

class ApiGetOneUserView(APIView):

    def get_user(self, pk, user = None):
        try:
            user = MyUser.objects.get(pk=pk)
            if user is not None:
                return user
            else:
                return None
        except MyUser.DoesNotExist:
            raise("El usuario no existe")
            
        

    def get(self, request, pk, format = None, user = None):
        user = self.get_user(pk=pk)
        user_serializer = MyUserSerializerGET(user)

        if user is not None:
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"User not found"}, status=status.HTTP_404_NOT_FOUND)
        

class ApiPostUserView(APIView):

    def get(self, request, format = None):
        format = {
            "username":"data(required)",
            "email":"data(required)",
            "password":"data(required)",
            "name":"data(not required)",
        }
        return Response(format, status=status.HTTP_200_OK)
    
    def post(self, request, format = None):
        
        user_serializer = MyUserSerializerPOST(data=self.request.data)
        try:
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"message":"Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"Los daros ingresados no son validos por favor revisalos"})
        except ValidationError:
            raise("Error con el user_serializer al ingresar la data")
        


    