# Generated by Django 4.2.6 on 2023-11-07 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_alter_book_anthology_alter_book_author_and_more'),
        ('basket', '0003_remove_order_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='catalog.book', verbose_name='Book'),
        ),
    ]
