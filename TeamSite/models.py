from django.db import models


class Players(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='Имя Фамилия')
    content = models.TextField(blank=True, verbose_name='Об игроке')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано(Дата)')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено(Дата)')
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Игрока'
        verbose_name_plural = 'Игроки'
        ordering = ['-created_at']


class Tournaments(models.Model):
    tournament = models.CharField(max_length=150, verbose_name='Название турнира')
    t_content = models.TextField(blank=True, verbose_name='О туринире')
    place = models.CharField(max_length=150, verbose_name='Место', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано(Дата)')
    photo = models.ImageField(upload_to='upload/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.tournament

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ['-created_at']
