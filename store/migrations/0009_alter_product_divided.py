# Generated by Django 4.2.7 on 2023-11-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_divided'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='divided',
            field=models.IntegerField(),
        ),
    ]
