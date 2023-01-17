from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    followed = serializers.ReadOnlyField(source="followed.username")

    class Meta:
        model = Follower
        fields = ["id", "owner", "followed", "created_at"]
