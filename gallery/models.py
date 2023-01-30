from django.db import models

from maincatalog.models import Product


# Create your models here.
class ProductPicture(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='продукт',
        related_name='get_images',
    )
    short_desc = models.TextField(
        verbose_name='описание',
        max_length=50,
        blank=True,
    )
    image = models.ImageField(
        upload_to='uploads/',
        verbose_name='изображение',
        blank=True,
    )
    is_main = models.BooleanField(
        verbose_name='основное',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='показывается',
        default=True,
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.short_desc} ({self.product})'
