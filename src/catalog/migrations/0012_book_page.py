# Generated by Django 4.2.6 on 2023-11-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='page',
            field=models.IntegerField(default=1, verbose_name='Number of pages'),
        ),
    ]
