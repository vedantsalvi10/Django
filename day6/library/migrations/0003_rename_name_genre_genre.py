# Generated by Django 5.1.7 on 2025-03-18 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_tittle_book_title_alter_book_publication_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='genre',
        ),
    ]
