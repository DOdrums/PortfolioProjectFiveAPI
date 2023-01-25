from rest_framework import generics, filters
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count("owner__post", distinct=True),
        songs_count=Count("owner__song", distinct=True),
    )
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["posts_count", "songs_count"]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retreive or update a profile if you're the owner
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
