from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    country = serializers.ReadOnlyField(source="country.name")
    posts_count = serializers.ReadOnlyField()
    songs_count = serializers.ReadOnlyField()

    status_name = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_status_name(self, obj):
        return obj.get_status_display()

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
            "status_name",
            "last_login",
            "date_joined",
            "posts_count",
            "songs_count",
        ]
