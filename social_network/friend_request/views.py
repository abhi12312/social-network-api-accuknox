from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from django.utils import timezone
from .models import FriendRequest, RequestStatus
from users.models import User
from .serializers import (
    FriendRequestCreateSerializer,
    FriendSerializer,
    FriendRequestSerializer
)

class FriendRequestViewSet(viewsets.GenericViewSet):
    queryset = FriendRequest.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def send_request(self, request, *args, **kwargs):
        to_user = User.objects.get(id=request.data['to_user'])

        # Checking if the users are already friends
        if FriendRequest.objects.filter(
            Q(from_user=request.user, to_user=to_user, status=RequestStatus.ACCEPTED) |
            Q(from_user=to_user, to_user=request.user, status=RequestStatus.ACCEPTED)
        ).exists():
            return Response({'error': 'You are already friends'}, status=status.HTTP_400_BAD_REQUEST)

        # Checking if there are too many friend requests in a short time
        if FriendRequest.objects.filter(from_user=request.user, created_at__gte=timezone.now() - timezone.timedelta(minutes=1)).count() >= 3:
            return Response({'error': 'Too many friend requests in a short time'}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        # Checking if a friend request has already been sent
        if FriendRequest.objects.filter(from_user=request.user, to_user=to_user, status=RequestStatus.PENDING).exists():
            return Response({'error': 'Friend request already sent'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FriendRequestCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(from_user=request.user)
            return Response({'message': 'Friend request sent'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def accept_request(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.to_user != request.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        instance.status = RequestStatus.ACCEPTED
        instance.save()
        return Response({'message': 'Friend request accepted'}, status=status.HTTP_200_OK)

    def reject_request(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.to_user != request.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        instance.status = RequestStatus.REJECTED
        instance.save()
        return Response({'message': 'Friend request rejected'}, status=status.HTTP_200_OK)

    def list_friends(self, request, *args, **kwargs):
        friends = FriendRequest.objects.filter(Q(from_user=request.user, status=RequestStatus.ACCEPTED) | Q(to_user=request.user, status=RequestStatus.ACCEPTED))
        friend_ids = [fr.from_user.id if fr.to_user == request.user else fr.to_user.id for fr in friends]
        friends_list = User.objects.filter(id__in=friend_ids)
        serializer = FriendSerializer(friends_list, many=True)
        return Response(serializer.data)

    def list_pending_requests(self, request, *args, **kwargs):
        pending_requests = FriendRequest.objects.filter(to_user=request.user, status=RequestStatus.PENDING)
        serializer = FriendRequestSerializer(pending_requests, many=True)
        return Response(serializer.data)
