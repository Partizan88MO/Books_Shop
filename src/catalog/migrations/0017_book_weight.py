# Generated by Django 4.2.6 on 2023-11-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='weight',
            field=models.IntegerField(default=1, verbose_name='Weight in gram'),
        ),
    ]
