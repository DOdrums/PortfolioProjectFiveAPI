from rest_framework import generics
from .models import Instrument
from .serializers import InstrumentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from melo_api.permissions import IsOwnerOrReadOnly


class InstrumentList(generics.ListCreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "owner__profile",
    ]


class InstrumentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive or destroy a post if you're the owner
    """

    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [IsOwnerOrReadOnly]
