from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status 
from django.contrib.auth.models import User
from .models import Subject, StudySession
from datetime import date
# Create your tests here.


class SubjectTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_subject(self):
        data = {'name': 'Math', 'description': 'Algebra'}
        response = self.client.post('/api/subjects/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_subjects(self):
        response = self.client.get('/api/subjects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_sees_only_subjects(self):
        other_user = User.objects.create_user(username='other', password='pass')
        self.client.force_authenticate(user=other_user)
        response = self.client.get('/api/subjects/')
        self.assertEqual(len(response.data), 0)


class StudySessionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.subject = Subject.objects.create(
            name='Math',
            user=self.user
        )
    
    def test_create_session(self):
        data = {
            'subject': self.subject.id,
            'title': 'Chapter1',
            'date': date.today(),
            'duration': 60
        }
        response = self.client.post('/api/sessions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_mark_session_complete(self):
        session = StudySession.objects.create(
            subject=self.subject,
            title='chapter1',
            date=date.today(),
            duration=60
        )
        response = self.client.patch(f'/api/sessions/{session.id}/complete/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_sessions_by_sbuject(self):
        subject2 = Subject.objects.create(name='Seience', user=self.user)
        StudySession.objects.create(
            subject=self.subject,
            title='Chapter 1',
            date=date.today(),
            duration=60
        )
        StudySession.objects.create(
            subject=subject2,
            title='Chapter2',
            date=date.today(),
            duration=60
        )
        response = self.client.get(f'/api/sessions/?subject={self.subject.id}')
        self.assertEqual(len(response.data), 1)


