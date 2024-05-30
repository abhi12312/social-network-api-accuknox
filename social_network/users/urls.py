from django.urls import path
from .views import SignupView, UserSearchView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='login'),
    path('users/', UserSearchView.as_view(), name='user-search'),
]