# Generated by Django 5.1.1 on 2024-11-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_articles_length_alter_articles_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='length',
            field=models.FloatField(blank=True, max_length=270, verbose_name='Длина товара'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='thickness',
            field=models.FloatField(blank=True, max_length=270, verbose_name='Толщина товара'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='weight',
            field=models.FloatField(blank=True, max_length=270, verbose_name='Вес товара'),
        ),
    ]
