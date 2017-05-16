from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username','first_name', 'last_name', 'password')
    """
    if misplace verification email.  Handle in view.
    """
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=30, default='', 
        required=False)
    last_name = serializers.CharField(max_length=30, default='', 
        required=False)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class PasswordResetVerifiedSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=128)


class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
