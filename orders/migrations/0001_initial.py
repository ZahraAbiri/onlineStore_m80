# Generated by Django 4.1.5 on 2023-02-01 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_alter_products_options_alter_products_count_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=10)),
                ('sum_price', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cus_id', to='users.user', verbose_name='cus_id')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pro_id', to='products.products', verbose_name='pro_id')),
            ],
            options={
                'verbose_name': 'ordes',
            },
        ),
    ]
