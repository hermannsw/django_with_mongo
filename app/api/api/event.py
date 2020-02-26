from rest_framework import viewsets

from app_api.models.event import Event
from app_api.serializers.eventserializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
