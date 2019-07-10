from ai_talks.models import Speaker
from rest_framework import serializers


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'
