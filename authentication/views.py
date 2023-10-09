from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import MyUser
from .serializers import MyUserSerializerGET
# Create your views here.

class ApiGetUserView(APIView):

    def get(self, request, format = None, users = None):
        users = MyUser.objects.all()
        users_serializer = MyUserSerializerGET(users, many = True)

        if users:
            return Response(users_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Users not found"}, status=status.HTTP_404_NOT_FOUND)
        
    