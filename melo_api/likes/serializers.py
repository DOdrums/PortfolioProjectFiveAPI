from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Like
        fields = [
            "id",
            "owner",
            "post",
            "created_at",
        ]
