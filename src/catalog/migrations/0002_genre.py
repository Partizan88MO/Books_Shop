# Generated by Django 4.2.6 on 2023-10-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name="Genre's name")),
                ('description', models.TextField(blank=True, null=True, verbose_name="Genre's description")),
            ],
        ),
    ]