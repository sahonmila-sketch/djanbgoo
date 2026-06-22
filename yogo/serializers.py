from rest_framwork import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username4', 'email4', 'name4', 'surname4']