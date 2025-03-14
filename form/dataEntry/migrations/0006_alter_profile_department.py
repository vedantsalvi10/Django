# Generated by Django 5.1.7 on 2025-03-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataEntry', '0005_alter_profile_department_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('bca', 'BCA'), ('ba', 'BA'), ('bcom', 'BCOM'), ('bba', 'BBA')], max_length=20),
        ),
    ]
