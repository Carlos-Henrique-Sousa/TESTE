from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Usuario

class LoginSerializer(serializers.Serializer):
    identificador = serializers.CharField()
    senha = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(identificador=data["identificador"], password=data["senha"])
        if not user:
            raise serializers.ValidationError("Identificador ou senha inválidos.")
        return {"user": user}
