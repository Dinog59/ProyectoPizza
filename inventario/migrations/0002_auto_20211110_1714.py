# Generated by Django 3.1.7 on 2021-11-10 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='inventario.inventoryaccount')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='media',
            name='product_inventory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productattributevalue',
            name='product_attribute',
        ),
        migrations.AlterUniqueTogether(
            name='productattributevalues',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='productattributevalues',
            name='attributevalues',
        ),
        migrations.RemoveField(
            model_name='productattributevalues',
            name='productinventory',
        ),
        migrations.RemoveField(
            model_name='productinventory',
            name='attribute_values',
        ),
        migrations.RemoveField(
            model_name='productinventory',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='productinventory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productinventory',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='product_inventory',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
        migrations.DeleteModel(
            name='ProductAttributeValue',
        ),
        migrations.DeleteModel(
            name='ProductAttributeValues',
        ),
        migrations.DeleteModel(
            name='ProductInventory',
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]