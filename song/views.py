from rest_framework import permissions, generics
from .models import Song
from .serializers import SongSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class SongList(generics.ListCreateAPIView):
    """
    List all songs or create a song if logged in.
    The perform_create method associates the song with the logged in user.
    """

    queryset = Song.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or destroy a song if you're the owner
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
