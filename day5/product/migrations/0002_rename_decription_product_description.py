# Generated by Django 5.1.7 on 2025-03-16 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='decription',
            new_name='description',
        ),
    ]
