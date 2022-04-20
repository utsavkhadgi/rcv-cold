# Generated by Django 3.2.11 on 2022-04-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]