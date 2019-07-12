from ai_talks.models import Speaker, Staff
from rest_framework import serializers


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        # fields = '__all__'
        fields = ('name','position','bio','abstract','image_path','date_and_time','talk_location','talk_title','id')


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        # fields = ('name','position','bio','abstract','image_path','date_and_time','talk_location','talk_title','id')
