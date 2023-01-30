from django.contrib import admin

from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'is_active',)
    list_display_links = ('name',)
    search_fields = ('name', 'description',)

# Register your models here.
admin.site.register(Page)
