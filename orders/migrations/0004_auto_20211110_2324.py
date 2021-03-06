# Generated by Django 3.1.7 on 2021-11-11 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20211110_2317'),
        ('orders', '0003_orderitem_inventory_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='store.product'),
        ),
    ]
