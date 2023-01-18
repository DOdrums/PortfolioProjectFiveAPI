from rest_framework import generics
from .models import Like
from .serializers import LikeSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retreive or destroy a post if you're the owner
    """

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
