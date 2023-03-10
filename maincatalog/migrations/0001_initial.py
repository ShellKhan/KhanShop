# Generated by Django 4.1.5 on 2023-01-18 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='название')),
                ('urlname', models.CharField(blank=True, max_length=300, unique=True, verbose_name='человекочитаемый url')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='показывается')),
                ('parentcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maincatalog.category')),
            ],
        ),
    ]
