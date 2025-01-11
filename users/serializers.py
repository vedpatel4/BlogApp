from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
import re

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'name', 'bio', 'picture', 'phone_number', 'password']


    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "A user with that email already exists."})

        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "A user with that username already exists."})

        password_errors = []
        if len(password) < 8:
            password_errors.append("Password must be at least 8 characters long.")
        if not re.findall('\d', password):
            password_errors.append("Password must contain at least one digit.")
        if not re.findall('[A-Z]', password):
            password_errors.append("Password must contain at least one uppercase letter.")
        if not re.findall('[a-z]', password):
            password_errors.append("Password must contain at least one lowercase letter.")
        if not re.findall('[^a-zA-Z0-9]', password):
            password_errors.append("Password must contain at least one special character.")

        if password_errors:
            raise serializers.ValidationError({"password": password_errors})

        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            bio=validated_data.get('bio', ''),
            picture=validated_data.get('picture', None),
            phone_number=validated_data.get('phone_number', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        user = authenticate(email=email, password=password)
        print(user)
        if user:
            if not user.is_active:
                raise serializers.ValidationError("User is deactivated.")
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("Unable to log in with provided credentials.")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'name', 'bio', 'picture', 'phone_number']

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

    def validate_new_password(self, value):
        # Add any custom password validation here
        return value