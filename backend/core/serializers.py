from rest_framework import serializers
from .models import Retreat, Mission, Meditation, Progress
from django.utils import timezone

class MeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditation
        fields = ['id', 'title', 'audio_url', 'duration_minutes']


class MissionSerializer(serializers.ModelSerializer):
    meditations = MeditationSerializer(many=True, read_only=True)

    class Meta:
        model = Mission
        fields = ['id', 'title', 'description', 'order', 'meditations']


class RetreatSerializer(serializers.ModelSerializer):
    missions = MissionSerializer(many=True, read_only=True)

    class Meta:
        model = Retreat
        fields = ['id', 'title', 'description', 'order', 'missions', 'unlocked_by_default']


class ProgressSerializer(serializers.ModelSerializer):
    meditation = MeditationSerializer(read_only=True)

    class Meta:
        model = Progress
        fields = ['id', 'meditation', 'completed', 'completed_at']
        read_only_fields = ['completed_at']

    def update(self, instance, validated_data):
        if validated_data.get("completed") and not instance.completed:
            instance.completed = True
            instance.completed_at = timezone.now()
            instance.save()
        return instance