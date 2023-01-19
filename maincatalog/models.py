from django.db import models


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
