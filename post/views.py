from django.db.models import Count
from rest_framework import permissions, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List all posts or create a post if logged in.
    The perform_create method associates the post with the logged in user.
    """

    queryset = Post.objects.annotate(
        comments_count=Count("comment", distinct=True),
    ).order_by("created_at")
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__followed__owner__profile",
        "owner__profile",
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or destroy a post if you're the owner
    """

    permission_classes = [IsOwnerOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    queryset = Post.objects.annotate(
        comments_count=Count("comment", distinct=True),
    ).order_by("created_at")
