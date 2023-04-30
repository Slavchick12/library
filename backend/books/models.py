from django.db import models
from users.models import User


class Author(models.Model):
    name = models.CharField('name', max_length=30)
    surname = models.CharField('surname', max_length=50)
    birth_date = models.DateField('birth date', db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_user', verbose_name='user')


class Book(models.Model):
    name = models.CharField('name', max_length=100, help_text='title of the book')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author', verbose_name='author')
    description = models.TextField('description', help_text='book description')
    pub_date = models.DateField('publication date', db_index=True)
