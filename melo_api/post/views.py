from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or destroy a post if you're the owner
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
