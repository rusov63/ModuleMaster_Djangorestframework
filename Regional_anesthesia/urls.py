from rest_framework.routers import DefaultRouter
from Regional_anesthesia.apps import RegionalAnesthesiaConfig
from django.urls import path
from Regional_anesthesia.views.modul import ModulViewSet

from Regional_anesthesia.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
LessonUpdateAPIView, LessonDestroyAPIView


app_name = RegionalAnesthesiaConfig.name

router = DefaultRouter()
router.register(r'anesthesia', ModulViewSet, basename='anesthesia')

urlpatterns = [

    # Lesson
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

] + router.urls
