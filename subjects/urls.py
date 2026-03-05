from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, StudySession, StudySessionViewSet

router = DefaultRouter()
router.register('subjects', SubjectViewSet, basename='subject')
router.register('sessions', StudySessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]


