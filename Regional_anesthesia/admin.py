from django.contrib import admin

from Regional_anesthesia.models import Modul, Lesson


@admin.register(Modul)
class ModulAdmin(admin.ModelAdmin):
    """
    Админ панель представляющее класс названия Модуля
    models.py/ class Modul.
    """

    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Админ панель представляющее класс название Занятие
    models.py/ class Lesson.
    """
    list_display = ('numbers', 'lessonNo', 'lesson', 'subject', 'form', 'hour')
    search_fields = ('lesson', 'subject')








