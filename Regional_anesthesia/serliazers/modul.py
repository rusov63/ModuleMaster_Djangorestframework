from rest_framework import serializers

from Regional_anesthesia.models import Modul


class ModulSerializer(serializers.ModelSerializer):
    """
    Класс описывающий модель Modul. Представляющий какие поля модели будут
    участвовать в процесссе сериализации.
    Наследование от базового класса ModelSerializer:
    """
    class Meta:
        model = Modul
        fields = '__all__'
