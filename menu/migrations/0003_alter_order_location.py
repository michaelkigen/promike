# Generated by Django 4.2.1 on 2023-12-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_order_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
