# Generated by Django 3.1.7 on 2021-11-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]