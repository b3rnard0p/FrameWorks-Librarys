# Generated by Django 5.1.5 on 2025-01-16 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_banner_remove_product_price_productattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattribute',
            name='status',
        ),
    ]
