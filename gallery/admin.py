from django.contrib import admin

from .models import ProductPicture, CategoryPicture


class ProductPictureAdmin(admin.ModelAdmin):
    list_display = ('product', 'short_desc', 'is_main', 'is_active',)
    list_display_links = ('short_desc',)
    search_fields = ('short_desc',)


class CategoryPictureAdmin(admin.ModelAdmin):
    list_display = ('product', 'short_desc', 'image',)
    list_display_links = ('short_desc',)
    search_fields = ('short_desc',)


# Register your models here.
admin.site.register(ProductPicture, ProductPictureAdmin)
admin.site.register(CategoryPicture, CategoryPictureAdmin)
