from django.test import TestCase

from Regional_anesthesia.models import Modul, Lesson


class LessonModelTest(TestCase):
    """
    Тесты для модели Lesson

    """

    def test_lesson(self):
        # Создаем объект Модуль для связи внешнего ключа
        modul = Modul.objects.create(name='Test Modul', is_active=True)

        # Создаем объект урока
        lesson = Lesson.objects.create(
            name=modul,
            numbers=1,
            lessonNo='LESSON ONE',
            lesson='Lesson 1',
            subject='Subject',
            description='Description',
            form='FORM ONE',
            hour='HOUR ONE'
        )

        # Проверяем что урок создан правильно
        self.assertEqual(lesson.numbers, 1)
        self.assertEqual(lesson.lessonNo, 'LESSON ONE')
        self.assertEqual(lesson.lesson, 'Lesson 1')
        self.assertEqual(lesson.subject, 'Subject')
        self.assertEqual(lesson.description, 'Description')
        self.assertEqual(lesson.form, 'FORM ONE')
        self.assertEqual(lesson.hour, 'HOUR ONE')
