from django.contrib import admin
from library.models import Book,Author,Genre
# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)