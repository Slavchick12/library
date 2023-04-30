from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Book, Author

admin.site.unregister(Group)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'birth_date')
    search_fields = ('name', 'surname', 'birth_date')
    list_filter = ('birth_date',)
    empty_value_display = '-empty-'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'description', 'pub_date')
    search_fields = ('name', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    empty_value_display = '-empty-'
