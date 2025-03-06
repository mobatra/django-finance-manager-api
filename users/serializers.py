from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    class Meta:
      model = User 
      fields = ['id', 'username', 'email', 'password']
      
      def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(username, email, password)
        return user
      