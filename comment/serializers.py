from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            "id",
            "owner",
            "is_owner",
            "post",
            "song",
            "content",
            "created_at",
            "updated_at",
        ]
