# Generated by Django 4.1.5 on 2023-01-18 15:50

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='название')),
                ('urlname', models.CharField(blank=True, max_length=300, unique=True, verbose_name='человекочитаемый url')),
                ('type', models.CharField(choices=[(pages.models.TypeChoice['TXT'], 'text'), (pages.models.TypeChoice['FRM'], 'form')], max_length=4, verbose_name='тип')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('content', models.TextField(blank=True, verbose_name='содержимое')),
                ('is_active', models.BooleanField(default=True, verbose_name='показывается')),
            ],
        ),
    ]
