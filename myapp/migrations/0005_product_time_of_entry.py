# Generated by Django 4.1 on 2022-08-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product_date_of_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time_of_entry',
            field=models.DateTimeField(null=True),
        ),
    ]
