# Generated by Django 5.2 on 2025-04-13 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_order_total_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
