from django.db import models
from django.db.models import ProtectedError

from khanshop.enums import StatusChoice


# Create your models here.
class CategoryQuerySet(models.QuerySet):
    def delete(self):
        for item in self:
            print(item.name, item.parentcategory)
            item.delete()


class Category(models.Model):
    objects = CategoryQuerySet.as_manager()
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
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='родительская категория',
    )
    is_active = models.BooleanField(
        verbose_name='показывается',
        default=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    @property
    def is_visible(self):
        if self.is_active:
            return self.parentcategory.is_visible if self.parentcategory else \
                True
        return False

    @property
    def parent_list(self):
        res = []
        if self.parentcategory:
            res = [self.parentcategory]
            res.extend(self.parentcategory.parent_list)
        return res

    def delete(self, new_link=None, **kwargs):
        if new_link:
            new_category = Category.objects.get(pk=new_link)
        elif self.parentcategory:
            new_category = self.parentcategory
        else:
            new_category = None
        if products := Product.objects.filter(category=self):
            if not new_category:
                raise ProtectedError(
                    f"{self} object can't be deleted because it isn`t empty",
                    self,
                )
            for product in products:
                product.category = new_category
                product.save()
        if subcats := Category.objects.filter(parentcategory=self):
            for subcat in subcats:
                subcat.parentcategory = new_category
                subcat.save()
        super().delete(**kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )
    name = models.CharField(
        verbose_name='название',
        max_length=200
    )
    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=400,
        blank=True
    )
    description = models.TextField(
        verbose_name='подробное описание',
        blank=True
    )
    price = models.DecimalField(
        verbose_name='цена',
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
        verbose_name='статус',
        max_length=3,
        choices=StatusChoice.choices,
    )
    is_active = models.BooleanField(
        verbose_name='показывается',
        default=True,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} ({self.category})'

    # Надо переделать, не устраивают меня такие статусы
    @property
    def get_status(self):
        return StatusChoice[self.status]

    @property
    def all_images(self):
        return self.get_images.filter(is_active=True)

    @property
    def main_image(self):
        return (
            gallery.filter(is_main=True).first() or gallery.first()
            if (gallery := self.all_images)
            else None
        )
