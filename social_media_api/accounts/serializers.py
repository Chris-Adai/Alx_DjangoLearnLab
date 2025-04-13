from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Post


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', 'bio', 'profile_picture')

    # password = serializers.CharField(write_only=True)
   # serializers.CharField(write_only=True)
    serializers.CharField()


    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # user = User.objects.create_user(
        #     username=validated_data['username'],
        #     email=validated_data.get('email'),
        #     password=validated_data['password']
        # )

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
         )

        # Create a token for the new user
        Token.objects.create(user=user)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    
# filepath: c:\DJANGO-PROJECTS\ALX_PROJECTS\social_media_api\accounts\serializers.py
#from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



