from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']  # O usuário será atribuído automaticamente

    def create(self, validated_data):
        request = self.context.get('request')  # Obtém o request do contexto

        if request and request.user.is_authenticated:
            validated_data['user'] = request.user  # Associa ao usuário autenticado
        else:
            raise serializers.ValidationError("Usuário não autenticado")

        return super().create(validated_data)
