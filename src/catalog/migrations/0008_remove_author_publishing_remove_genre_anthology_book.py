# Generated by Django 4.2.6 on 2023-11-04 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_author_publishing_genre_anthology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='publishing',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='anthology',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Book name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Book description')),
                ('anthology', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='catalog.anthology', verbose_name='Anthology')),
                ('publishing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='catalog.publishing', verbose_name='Publishing')),
            ],
        ),
    ]
