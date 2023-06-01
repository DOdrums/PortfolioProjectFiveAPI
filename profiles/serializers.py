from rest_framework import serializers
from django_countries import countries
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    following_id = serializers.SerializerMethodField()
    country = serializers.ReadOnlyField(source="country.name")
    posts_count = serializers.ReadOnlyField()
    songs_count = serializers.ReadOnlyField()
    status_choices = serializers.SerializerMethodField()
    country_choices = serializers.SerializerMethodField()

    status_name = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_status_name(self, obj):
        return obj.get_status_display()

    def get_country_choices(sefl, obj):
        return dict(countries)

    def get_status_choices(self, obj):
        return dict(Profile.STATUS)

    def get_following_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None

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
            "following_id",
            "last_login",
            "date_joined",
            "posts_count",
            "songs_count",
            "status_choices",
            "country_choices",
        ]
