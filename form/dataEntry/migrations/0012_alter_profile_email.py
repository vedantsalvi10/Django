# Generated by Django 5.1.7 on 2025-03-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataEntry', '0011_alter_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
