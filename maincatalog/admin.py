from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)
    list_display_links = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'is_active', 'price',
                    'quantity',)
    list_display_links = ('name',)
    search_fields = ('name', 'category',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
