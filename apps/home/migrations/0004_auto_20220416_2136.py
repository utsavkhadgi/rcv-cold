# Generated by Django 3.2.11 on 2022-04-16 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
