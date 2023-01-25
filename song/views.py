from rest_framework import generics
from .models import Song
from .serializers import SongSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or destroy a song if you're the owner
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
