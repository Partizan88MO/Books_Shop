# Generated by Django 4.2.6 on 2023-11-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_book_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity available'),
        ),
    ]