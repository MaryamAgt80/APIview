from django.contrib import admin

from .models import Book


class adminbook(admin.ModelAdmin):
    list_display = ['name', 'store_name']
    list_filter = ['name','store_name']


admin.site.register(Book, adminbook)