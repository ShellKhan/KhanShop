# Generated by Django 4.1.5 on 2023-01-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='type',
            field=models.CharField(choices=[('TXT', 'text'), ('FRM', 'form')], max_length=3, verbose_name='тип'),
        ),
    ]
