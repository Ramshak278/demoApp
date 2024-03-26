from django.contrib.auth import password_validation, authenticate
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("Id","email","creation_time","deletion_time","isDeleted","firstName","lastName","password")
        extra_kwargs={"password":{"write_only":True}}
    def validate_password(self,value):
        password_validation.validate_password(value,self.instance)
        return value
    @staticmethod
    def validate_email(value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return  value
    def create(self,validated_data):
        email = validated_data.get("email")
        password = validated_data.pop("password")
        user=User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class RegisterDataSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    firstName = serializers.CharField(required=True)
    lastName = serializers.CharField(required=True)


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        username_or_email=attrs.get(self.username_field)
        user = User.objects.filter(**{f'{self.username_field}__iexact':username_or_email}).first()
        if user:
            attrs[self.username_field]=getattr(user,self.username_field)
        #super().is_valid(raise_exception=True)
        data=super().validate(attrs)
        serializer = UserSerializer(self.user)
        data = {**serializer.data,
                "Token":data['access']}
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Id', "email","creation_time","deletion_time","isDeleted","firstName","lastName" ]
        extra_kwargs = {'password': {'write_only': True}}

