from rest_framework import serializers

from Regional_anesthesia.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Класс описывающий модель Lesson. Представляющий какие поля модели будут
    участвовать в процесссе сериализации.
    Наследование от базового класса ModelSerializer:
    """
    class Meta:
        model = Lesson
        fields = '__all__'
