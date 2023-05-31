from django.db.models import Count
from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Song
from .serializers import SongSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class SongList(generics.ListCreateAPIView):
    """
    List all songs or create a song if logged in.
    The perform_create method associates the song with the logged in user.
    """

    queryset = Song.objects.annotate(
        comments_count=Count("comment", distinct=True),
        mics_count=Count("mic", distinct=True),
    ).order_by("created_at")
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        "mics_count",
    ]
    filterset_fields = [
        "owner__followed__owner__profile",
        "mic__owner__profile",
        "owner__profile",
    ]

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

    queryset = Song.objects.annotate(
        comments_count=Count("comment", distinct=True),
        mics_count=Count("mic", distinct=True),
    ).order_by("created_at")
