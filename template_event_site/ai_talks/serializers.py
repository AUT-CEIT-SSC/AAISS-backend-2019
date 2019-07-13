from ai_talks.models import Speaker, Staff, StaticParts, ScientificCommittee
from rest_framework import serializers


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        # fields = '__all__'
        fields = ('name', 'position', 'bio', 'abstract', 'image_path', 'date_and_time', 'talk_location', 'talk_title', 'id', 'sort')


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        # fields = ('name','position','bio','abstract','image_path','date_and_time','talk_location','talk_title','id')


class ScientificCommitteeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScientificCommittee
        fields = '__all__'


class StaticPartsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaticParts
        fields = '__all__'
