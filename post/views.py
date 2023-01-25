from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or destroy a post if you're the owner
    """

    permission_classes = [IsOwnerOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
