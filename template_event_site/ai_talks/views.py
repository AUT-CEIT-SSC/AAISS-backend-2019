from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ai_talks.models import Speaker
# Create your views here.
from ai_talks.serializers import UserSerializer, GroupSerializer, SpeakerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SpeakerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
