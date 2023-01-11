from rest_framework import generics
from .models import Song
from .serializers import SongSerializer


class PostList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or destroy a song if you're the owner
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer
