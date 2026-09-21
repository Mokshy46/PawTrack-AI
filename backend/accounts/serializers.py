from .models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class UserModelSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only = True, min_length = 8)
    
    
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "role",
        ]
        
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["email"],
            **validated_data,
        )