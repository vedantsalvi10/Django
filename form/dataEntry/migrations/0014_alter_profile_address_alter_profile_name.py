# Generated by Django 5.1.7 on 2025-03-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataEntry', '0013_remove_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
