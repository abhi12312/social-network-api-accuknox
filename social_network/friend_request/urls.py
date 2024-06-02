from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FriendRequestViewSet

router = DefaultRouter()
router.register(r'friend-requests', FriendRequestViewSet, basename='friend-request')

urlpatterns = [
    path('', include(router.urls)),
    path('friend-requests/send/', FriendRequestViewSet.as_view({'post': 'send_request'}), name='send-friend-request'),
    path('friend-requests/<int:pk>/accept/', FriendRequestViewSet.as_view({'put': 'accept_request'}), name='accept-friend-request'),
    path('friend-requests/<int:pk>/reject/', FriendRequestViewSet.as_view({'put': 'reject_request'}), name='reject-friend-request'),
    path('friends/', FriendRequestViewSet.as_view({'get': 'list_friends'}), name='list-friends'),
    path('pending-requests/', FriendRequestViewSet.as_view({'get': 'list_pending_requests'}), name='list-pending-requests'),
]
