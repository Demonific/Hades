# Generated by Django 3.2 on 2022-05-31 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hades', '0005_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
    ]
