from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username3', 'email3', 'name3', 'surname3']