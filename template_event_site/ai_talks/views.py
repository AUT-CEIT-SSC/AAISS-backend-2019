from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ai_talks.models import Speaker
# Create your views here.
from ai_talks.serializers import SpeakerSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows speakers to be viewed or edited.
    """
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
