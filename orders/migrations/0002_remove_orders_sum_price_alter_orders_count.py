# Generated by Django 4.1.5 on 2023-02-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='sum_price',
        ),
        migrations.AlterField(
            model_name='orders',
            name='count',
            field=models.IntegerField(),
        ),
    ]
