from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import MyUser


class MyUserSerializerGET(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'email']


class MyUserSerializerPOST(ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"

    
    def create(self, validate_data):
        user = MyUser(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
    
