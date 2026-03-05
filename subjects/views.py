from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Subject, StudySession
from .serializers import SubjectSerializer, StudySessionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudySessionViewSet(viewsets.ModelViewSet):
    serializer_class = StudySessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudySession.objects.filter(subject__user=self.request.user)
    
    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        session = self.get_object()
        session.is_completed = True
        session.save()
        return Response({'status': 'session marked as completed'})
    


