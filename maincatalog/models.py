from django.db import models

from khanshop.enums import StatusChoice


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=200,
        unique=True
    )
    urlname = models.CharField(
        verbose_name='человекочитаемый url',
        max_length=300,
        unique=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    parentcategory = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name='показывается',
        default=True,
    )

    @property
    def is_visible(self):
        if self.is_active:
            if self.parentcategory:
                return self.parentcategory.is_visible
            else:
                return True
        return False

    @property
    def parent_list(self):
        res = []
        if self.parentcategory:
            res = [self.parentcategory]
            res.extend(self.parentcategory.parent_list)
        return res
# переделываем delete()


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
        null=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое описание продукта',
        max_length=300,
        blank=True
    )
    description = models.TextField(
        verbose_name='описание продукта',
        blank=True
    )
    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=0,
        null=True,
        default=None
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0
    )
    status = models.CharField(
        verbose_name='тип',
        max_length=100,
        choices=[(tag, tag.value) for tag in StatusChoice],
    )
# переделываем __init__() или добавляем @property с параметрами, чтобы
# генерировались картинки заданного размера
