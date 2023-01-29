from django.contrib import admin

from .models import Category, Product, ProductPicture


class CategoryAdmin(admin.ModelAdmin) :
    list_display = ('name', 'is_active',)
    list_display_links = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin) :
    list_display = ('name', 'category', 'status', 'is_active', 'price',
                    'quantity',)
    list_display_links = ('name',)
    search_fields = ('name', 'category',)


class ProductPictureAdmin(admin.ModelAdmin) :
    list_display = ('product', 'short_desc', 'is_main', 'is_active',)
    list_display_links = ('short_desc',)
    search_fields = ('short_desc',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPicture, ProductPictureAdmin)
