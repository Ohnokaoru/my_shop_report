# Generated by Django 5.1.1 on 2024-09-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sales_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
