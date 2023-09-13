from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Modul(models.Model):
    """
    Класс названия модуля.
    """

    name = models.CharField(max_length=200, verbose_name='Название Общеобразовательного модуля')
    is_active = models.BooleanField(default=True, verbose_name='активный')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Добавить Модуль'
        verbose_name_plural = 'Модули'
        ordering = ('name',)


class Lesson(models.Model):
    """
    Класс описывающее - Занятие.
    """
    LESSON = [
        ('LESSON ONE', 'Занятие 1.'),
        ('LESSON TWO', 'Занятие 2.'),
        ('LESSON THREE', 'Занятие 3.'),
        ('LESSON FOUR', 'Занятие 4.'),
        ('LESSON FIVE', 'Занятие 5.'),
    ]

    FORM = [
        ('FORM ONE', 'Обзорная лекция.'),
        ('FORM TWO', 'Лекция.'),
        ('FORM THREE', 'Практикум.'),
        ('FORM FOUR', 'Консультация.'),
        ('FORM FIVE', 'Беседа.'),
        ('FORM SIX', 'Круглый стол.'),
    ]

    HOUR = [
        ('HOUR ONE', '1 час.'),
        ('HOUR TWO', '2 часа.'),
        ('HOUR THREE', '3 часа.'),
        ('HOUR FOUR', '4 часа.')
    ]

    name = models.ForeignKey(Modul, on_delete=models.CASCADE, verbose_name='Название общего курса')
    numbers = models.PositiveSmallIntegerField(verbose_name='Порядковый номер')
    lessonNo = models.CharField(choices=LESSON, verbose_name='Занятие')
    lesson = models.CharField(max_length=200, verbose_name='Название занятия')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    description = models.TextField(verbose_name='Описание')
    form = models.CharField(max_length=20, choices=FORM, verbose_name='Форма проведения', **NULLABLE)
    hour = models.CharField(max_length=20, choices=HOUR, verbose_name='Количество часов', **NULLABLE)
    image = models.ImageField(upload_to='lesson/', verbose_name='Изображение', **NULLABLE)

    class Meta:
        verbose_name = 'Добавить занятие'
        verbose_name_plural = 'Занятия'
        ordering = ('lesson',)

    def __str__(self):
        return f'{self.numbers} - {self.lessonNo} - {self.lesson} - {self.subject} - {self.form} - {self.hour}'
