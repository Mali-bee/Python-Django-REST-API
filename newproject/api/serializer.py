#to transform model into a Json data to be accessible to the API

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = '__all__'
        