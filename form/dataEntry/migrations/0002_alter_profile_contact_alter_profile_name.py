# Generated by Django 5.1.7 on 2025-03-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataEntry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
