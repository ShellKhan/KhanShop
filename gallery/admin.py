from django.contrib import admin

from .models import ProductPicture


class ProductPictureAdmin(admin.ModelAdmin):
    list_display = ('product', 'short_desc', 'is_main', 'is_active',)
    list_display_links = ('short_desc',)
    search_fields = ('short_desc',)


# Register your models here.
admin.site.register(ProductPicture, ProductPictureAdmin)
