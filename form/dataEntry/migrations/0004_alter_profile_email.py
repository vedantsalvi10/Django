# Generated by Django 5.1.7 on 2025-03-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataEntry', '0003_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
