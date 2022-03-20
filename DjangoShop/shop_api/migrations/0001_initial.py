# Generated by Django 4.0.3 on 2022-03-20 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.TextField(max_length=100)),
                ('cost', models.FloatField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.categories')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.salesman')),
            ],
        ),
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_first', models.BooleanField()),
                ('photo', models.ImageField(upload_to='product-images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.product')),
            ],
        ),
    ]