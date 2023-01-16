from rest_framework import generics
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retreive, or destroy a comment if you're the owner
    """

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
