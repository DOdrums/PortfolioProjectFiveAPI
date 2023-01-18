from rest_framework import serializers
from .models import Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Instrument
        fields = [
            "id",
            "owner",
            "instrument",
            "experience",
            "created_at",
        ]
