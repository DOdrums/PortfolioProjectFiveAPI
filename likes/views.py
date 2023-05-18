from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    """
    List all likes or create a like if a user is logged in
    The perform_create method associates the like with the logged in user.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retreive or destroy a post if you're the owner
    """

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
