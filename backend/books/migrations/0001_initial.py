# Generated by Django 4.2 on 2023-04-30 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('surname', models.CharField(max_length=50, verbose_name='surname')),
                ('birth_date', models.DateField(db_index=True, verbose_name='birth date')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='title of the book', max_length=100, verbose_name='name')),
                ('description', models.TextField(help_text='book description', verbose_name='description')),
                ('pub_date', models.DateField(db_index=True, verbose_name='publication date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='books.author', verbose_name='author')),
            ],
        ),
    ]
