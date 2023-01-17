from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    country = serializers.ReadOnlyField(source="country.name")
    posts_count = serializers.ReadOnlyField()
    songs_count = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "name",
            "subname",
            "contact_info",
            "description",
            "avatar",
            "country",
            "status",
            "last_login",
            "date_joined",
            "posts_count",
            "songs_count",
        ]
