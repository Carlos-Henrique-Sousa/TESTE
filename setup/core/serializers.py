from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

user = get_user_model()

class UserSerializer(ModelSerializer):
  class Meta:
    model = user
    fields = ('id', 'username', 'email', 'profile', 'first_name', 'last_name')
    read_only_fields = ('id',)