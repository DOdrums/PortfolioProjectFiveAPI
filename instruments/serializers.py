from rest_framework import serializers
from .models import Instrument
from .instruments import INSTRUMENTS


class InstrumentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    instrument_name = serializers.SerializerMethodField()
    experience_name = serializers.SerializerMethodField()
    instrument_choices = serializers.SerializerMethodField()

    def get_instrument_name(self, obj):
        return obj.get_instrument_display()

    def get_experience_name(self, obj):
        return obj.get_experience_display()

    def get_instrument_choices(self, ojb):
        return dict(INSTRUMENTS)

    class Meta:
        model = Instrument
        fields = [
            "id",
            "owner",
            "instrument",
            "instrument_name",
            "experience",
            "experience_name",
            "created_at",
            "instrument_choices",
        ]
