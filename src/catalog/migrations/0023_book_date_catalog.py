# Generated by Django 4.2.6 on 2023-11-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_book_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_catalog',
            field=models.DateField(auto_now=True, verbose_name='date of catalogin'),
        ),
    ]
