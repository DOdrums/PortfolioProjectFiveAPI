from rest_framework import serializers
from .models import Mic


class MicSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Mic
        fields = [
            "id",
            "owner",
            "song",
            "created_at",
        ]
