from django.db import models
from django.forms import ModelForm

# Create your models here.

class Films(models.Model):
    name = models.CharField('Название', max_length=50, default='Film_name')
    short_description = models.CharField('Описание фильма', max_length=300)
    text = models.TextField('Отзыв о фильме')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв о фильме'
        verbose_name_plural = 'Отзывы о фильмах'

