from rest_framework import serializers
from .models import Song
from mics.models import Mic


class SongSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.avatar.url")
    mic_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    mics_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_mic_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            mic = Mic.objects.filter(owner=user, post=obj).first()
            return mic.id if mic else None
        return None

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
            "profile_id",
            "profile_image",
            "comments_count",
            "mics_count",
            "mic_id",
        ]
