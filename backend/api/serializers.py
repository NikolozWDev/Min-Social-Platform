from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']
    
    def validate(self, data):
        forbidden = ["!", "@", "#", "$", "%", "^", "&", "*",
                    "(", ")", "_", "-", "+", "=", "[", "]",
                    "{", "}", ";", ":", "'", "/", '"', ",", ".",
                    "<", ">", "?", "|", "`", "~", " "]
        if len(data["username"]) > 16 or len(data["username"]) < 4 or data["username"].strip() != data["username"] or any(str(ch) in data["username"] for ch in forbidden):
            raise serializers.ValidationError("Incorrect Username")
        if not "@" in data["email"]:
            raise serializers.ValidationError("Incorrect Email")
        if len(data["password"]) > 16 or len(data["password"]) < 6 or data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Incorrect Password")
        return data
    
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = CustomUser.objects.create_user(
            username = validated_data.get("username", ""),
            email = validated_data["email"],
            password = validated_data["password"]
        )
        return user


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Error Email Or Password")
        
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Email Does Not Exist")
        
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid Credentials")
        
        return super().validate({"email": email, "password": password})


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'followers' 'date_joined']