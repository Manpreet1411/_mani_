# Generated by Django 4.1.1 on 2022-09-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_shoppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_pic2',
            field=models.ImageField(blank=True, null=True, upload_to='shoes_photos'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_pic3',
            field=models.ImageField(blank=True, null=True, upload_to='shoes_photos'),
        ),
    ]