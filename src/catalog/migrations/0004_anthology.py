# Generated by Django 4.2.6 on 2023-10-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_publishing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anthology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name="Anthology's name")),
                ('description', models.TextField(blank=True, null=True, verbose_name="Anthology's description")),
            ],
        ),
    ]
