from rest_framework import status
from rest_framework.test import APITestCase

from Regional_anesthesia.models import Modul
from Regional_anesthesia.serliazers.modul import ModulSerializer


class ModulApiTestCase(APITestCase):
    """
    Тестирование запроса к API /anesthesia/.
    """

    def test_get(self):
        # Тестирование GET-запроса к API

        modul_1 = Modul.objects.create(name='test 1', is_active=True)
        modul_2 = Modul.objects.create(name='test 2', is_active=False)
        url = 'http://127.0.0.1:8000/anesthesia/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = ModulSerializer([modul_1, modul_2], many=True).data
        self.assertEqual(response.data, serializer_data)
        print(response.data)

    def test_post(self):
        # Тестирование POST-запроса к API

        self.data = {"name": "Региональная анестезия", "is_active": True}
        self.url = 'http://127.0.0.1:8000/anesthesia/'
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)


    def test_delete(self):
        # Тестирование DELETE-запроса к API

        url = 'http://127.0.0.1:8000/anesthesia/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


