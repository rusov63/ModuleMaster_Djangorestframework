from rest_framework.test import APITestCase, APIClient

from Regional_anesthesia.models import Modul


class LessonApiTestCase(APITestCase):
    """
    Тестирование urls - lessons API.
    """

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.client = APIClient()
        self.modul = Modul.objects.create(name='Test Modul', is_active=True)

    def test_get(self):
        # Тестирование GET-запроса к API

        url = 'http://127.0.0.1:8000/lessons/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        # Тестирование POST-запроса к API

        self.lesson = {
            'name': self.modul.id,
            'numbers': 1,
            'lessonNo': 'LESSON ONE',
            'lesson': 'Test Lesson',
            'subject': 'Test Subject',
            'description': 'Test Description',
            'form': 'FORM ONE',
            'hour': 'HOUR ONE'
        }
        self.url = 'http://127.0.0.1:8000/lessons/create/'
        response = self.client.post(self.url, self.lesson, format='json')
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        # Тестирование DELETE-запроса к API
        self.lesson = {
            'name': self.modul.id,
            'numbers': 1,
            'lessonNo': 'LESSON ONE',
            'lesson': 'Test Lesson',
            'subject': 'Test Subject',
            'description': 'Test Description',
            'form': 'FORM ONE',
            'hour': 'HOUR ONE'
        }

        self.url = 'http://127.0.0.1:8000/lessons/delete/'
        response = self.client.post(self.url, self.lesson, format='json')
        self.assertEqual(response.status_code, 404)
