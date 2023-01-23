from django.db import models
from django.db.models import ProtectedError

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
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='родительская категория',
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

    def delete(self, new_link=None, **kwargs):
        if new_link:
            new_category = Category.objects.get(pk=new_link)
        elif self.parentcategory:
            new_category = self.parentcategory
        else:
            new_category = None
        subcats = Category.objects.filter(parentcategory=self)
        if subcats:
            for subcat in subcats:
                subcat.parentcategory = new_category
                subcat.save()
        products = Product.objects.filter(category=self)
        if products:
            if new_category:
                for product in products:
                    product.category = new_category
                    product.save()
            else:
                raise ProtectedError(
                    "%s object can't be deleted because it isn`t empty" % (
                        self.name)
                )
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
        max_length=100,
        choices=[(tag, tag.value) for tag in StatusChoice],
    )
# убираем поле с картинкой, делаем класс для картинок с генерацией картинки
# нужного размера по параметрам
