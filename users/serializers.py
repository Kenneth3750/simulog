from rest_framework import serializers
from .functions import verify_email

class UserEmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)

    def validate_email(self, value):
        is_valid = verify_email(value)
        if not is_valid:
            raise serializers.ValidationError('The user does not have authorization to use the application')
        return value
    
class UsersListSerializer(serializers.Serializer):
    users = serializers.ListField(child=serializers.CharField(max_length=200))








