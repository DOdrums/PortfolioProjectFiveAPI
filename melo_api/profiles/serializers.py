from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    country = serializers.ReadOnlyField(source="country.name")
    posts_count = serializers.ReadOnlyField()
    songs_count = serializers.ReadOnlyField()

    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "is_owner",
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
