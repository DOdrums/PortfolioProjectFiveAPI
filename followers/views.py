from rest_framework import generics
from .models import Follower
from .serializers import FollowerSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retreive, or destroy a comment if you're the owner
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
