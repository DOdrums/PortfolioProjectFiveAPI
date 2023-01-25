from rest_framework import generics
from .models import Instrument
from .serializers import InstrumentSerializer
from melo_api.permissions import IsOwnerOrReadOnly


class InstrumentList(generics.ListAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer


class InstrumentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive or destroy a post if you're the owner
    """

    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [IsOwnerOrReadOnly]
