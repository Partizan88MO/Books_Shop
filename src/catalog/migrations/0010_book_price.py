# Generated by Django 4.2.6 on 2023-11-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_book_author_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=1.0, verbose_name='Price BYN'),
        ),
    ]
