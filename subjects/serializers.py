from rest_framework import serializers
from .models import Subject, StudySession

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['created_at']

class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields = ['id', 'subject', 'title', 'date', 'duration', 'is_completed', 'notes', 'created_at']
        read_only_fields = ['created_at']
