from rest_framework import generics, permissions
from .models import Mic
from .serializers import MicSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class MicList(generics.ListCreateAPIView):
    """
    List all mics or create a mic if a user is logged in.
    The perform_create method associates the mic with the logged in user.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Mic.objects.all()
    serializer_class = MicSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MicDetail(generics.RetrieveDestroyAPIView):
    """
    Retreive or destroy a post if you're the owner
    """

    queryset = Mic.objects.all()
    serializer_class = MicSerializer
    permission_classes = [IsOwnerOrReadOnly]
