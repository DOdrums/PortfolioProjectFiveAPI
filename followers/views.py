from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers: all instances of a user
    following another user.
    Create a follower with the perform_create function
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retreive, or destroy a comment if you're the owner
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
