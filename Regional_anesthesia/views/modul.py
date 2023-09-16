from rest_framework import viewsets

from Regional_anesthesia.models import Modul
from Regional_anesthesia.serliazers.modul import ModulSerializer


class ModulViewSet(viewsets.ModelViewSet):
    """
    Описание ViewSet для работы с сериализатором ModulSerializer.
    Предоставляет метод: list, create, retrieve, update,partial_update,destroy.
    Наследуется от ModelViewSet.
    """

    serializer_class = ModulSerializer
    queryset = Modul.objects.all()
