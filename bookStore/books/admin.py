from django.contrib import admin

# Register your models here.

from books.models import book
admin.site.register(book)
