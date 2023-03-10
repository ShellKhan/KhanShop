from django.db import models

from khanshop.enums import TypeChoice


# Create your models here.
class Page(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=200,
        unique=True,
    )
    urlname = models.SlugField(
        verbose_name='человекочитаемый url',
        max_length=300,
        unique=True,
        blank=True,
    )
    type = models.CharField(
        verbose_name='тип',
        max_length=3,
        choices=TypeChoice.choices,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    content = models.TextField(
        verbose_name='содержимое',
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='показывается',
        default=True
    )

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return f'{self.name} ({self.type})'
