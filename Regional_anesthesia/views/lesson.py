from rest_framework import generics

from Regional_anesthesia.models import Lesson
from Regional_anesthesia.serliazers.lesson import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Отвечает за создание сущности в модели Lesson.
    Наследование от CreateAPIView.
    """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """
    Отвечает за получение списка сущностей в модели Lesson.
    Наследование от ListAPIView.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()



class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отвечает за получение одной сущности в модели Lesson.
    Наследование от RetrieveAPIView.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Отвечает за обновление сущности в модели Lesson.
    Наследование от UpdateAPIView.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # lookup_field = 'pk'
    # lookup_url_kwarg = 'pk'
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    # throttle_classes = [UserRateThrottle]
    # throttle_scope = 'user'

class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Отвечает за удаление сущности в модели Lesson.
    Наследование от DestroyAPIView.
    """
    queryset = Lesson.objects.all
