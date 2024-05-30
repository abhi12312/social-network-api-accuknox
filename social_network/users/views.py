from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User
from .serializers import SignupSerializer, UserSerializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10

class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['email', 'name']
    pagination_class = CustomPagination

