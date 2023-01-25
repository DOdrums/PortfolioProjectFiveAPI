from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Song
        fields = [
            "id",
            "owner",
            "is_owner",
            "title",
            "description",
            "audio",
            "created_at",
            "updated_at",
        ]
