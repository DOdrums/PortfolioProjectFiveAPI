from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or destroy a song if you're the owner
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
