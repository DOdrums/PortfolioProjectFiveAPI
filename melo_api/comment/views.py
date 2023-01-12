from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or destroy a song if you're the owner
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
