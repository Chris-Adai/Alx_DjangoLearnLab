from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, PostSerializer
from django.contrib.auth import get_user_model
# from posts.models import Post
from .models import Post, User, CustomUser

##
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

# 
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.followers.add(user_to_follow)
        return Response({'status': 'following'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()
        request.user.followers.remove(user_to_unfollow)
        return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # following_users = self.request.user.followers.all()
        # return Post.objects.filter(author__in=following_users).order_by('-created_at')

    # Get the users the current user is following
        following_users = self.request.user.following.all()
        # Filter posts by authors in the following list and order by creation date
        # return Post.objects.filter(author__in=following_users).order_by('-created_at')
        return Post.objects.filter(author__in=following_users).order_by()
        
#
class UserListView(generics.GenericAPIView):
    """
    A view to list all users.
    """
    # queryset = User.objects.all()  # CustomUser
    queryset = CustomUser.objects.all()  # CustomUser

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
