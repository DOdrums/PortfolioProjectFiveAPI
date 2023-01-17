from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Comment
        fields = ["id", "owner", "post", "song", "content", "created_at", "updated_at"]
