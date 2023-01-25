from rest_framework import generics
from .models import Mic
from .serializers import MicSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class MicList(generics.ListAPIView):
    queryset = Mic.objects.all()
    serializer_class = MicSerializer


class MicDetail(generics.RetrieveDestroyAPIView):
    """
    Retreive or destroy a post if you're the owner
    """

    queryset = Mic.objects.all()
    serializer_class = MicSerializer
    permission_classes = [IsOwnerOrReadOnly]
