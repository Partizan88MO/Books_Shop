# Generated by Django 4.2.6 on 2023-11-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_alter_book_anthology_alter_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, default=1, to='catalog.author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, default=1, to='catalog.genre', verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Book name'),
        ),
    ]