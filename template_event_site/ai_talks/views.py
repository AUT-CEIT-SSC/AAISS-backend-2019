from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ai_talks.models import Speaker, Staff, StaticParts, ScientificCommittee
# Create your views here.
from ai_talks.serializers import SpeakerSerializer, StaffSerializer, ScientificCommitteeSerializer, StaticPartsSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows speakers to be viewed or edited.
    """
    queryset = Speaker.objects.all().order_by('sort')
    serializer_class = SpeakerSerializer


class StaffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows speakers to be viewed or edited.
    """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaticPartsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows speakers to be viewed or edited.
    """
    queryset = StaticParts.objects.all()
    serializer_class = StaticPartsSerializer


class ScientificCommitteeViewSet(viewsets.ModelViewSet):
    queryset = ScientificCommittee.objects.all()
    serializer_class = ScientificCommitteeSerializer
