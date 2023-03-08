from django.db import models

from khanshop import customization
from .utils import make_sized_image
from maincatalog.models import Product, Category


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
        verbose_name = 'Изображения продуктов'
        verbose_name_plural = 'Изображения продуктов'

    def __str__(self):
        return f'{self.short_desc} ({self.product})'

    @property
    def get_catalog_image(self):
        return make_sized_image(self, customization.CATALOG_SIZE_W,
                                customization.CATALOG_SIZE_H)

    @property
    def get_gallery_image(self):
        return make_sized_image(self, customization.GALLERY_SIZE_W,
                                customization.GALLERY_SIZE_H)

    @property
    def get_main_image(self):
        return make_sized_image(self, customization.MAIN_SIZE_W,
                                customization.MAIN_SIZE_H)

    @property
    def get_big_image(self):
        return make_sized_image(self, customization.BIG_SIZE_W,
                                customization.BIG_SIZE_H)


class CategoryPicture(models.Model):
    product = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
        related_name='get_images',
        primary_key=True,
    )
    short_desc = models.TextField(
        verbose_name='описание',
        max_length=50,
        blank=True,
    )
    image = models.ImageField(
        upload_to='uploads/category/',
        verbose_name='изображение',
        blank=True,
    )

    class Meta:
        verbose_name = 'Изображение категорий'
        verbose_name_plural = 'Изображение категорий'

    def __str__(self):
        return f'{self.short_desc} ({self.product})'

    @property
    def get_catalog_image(self):
        return make_sized_image(self, customization.CATALOG_SIZE_W,
                                customization.CATALOG_SIZE_H)

    @property
    def get_gallery_image(self):
        return make_sized_image(self, customization.GALLERY_SIZE_W,
                                customization.GALLERY_SIZE_H)

    @property
    def get_main_image(self):
        return make_sized_image(self, customization.MAIN_SIZE_W,
                                customization.MAIN_SIZE_H)

    @property
    def get_big_image(self):
        return make_sized_image(self, customization.BIG_SIZE_W,
                                customization.BIG_SIZE_H)
