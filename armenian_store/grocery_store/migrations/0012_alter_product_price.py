# Generated by Django 4.1.2 on 2022-10-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_store', '0011_alter_product_composition_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]
