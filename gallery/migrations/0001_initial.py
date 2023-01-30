# Generated by Django 4.1.5 on 2023-01-30 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maincatalog', '0014_delete_productpicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_desc', models.TextField(blank=True, max_length=50, verbose_name='описание')),
                ('image', models.ImageField(blank=True, upload_to='uploads/', verbose_name='изображение')),
                ('is_main', models.BooleanField(default=False, verbose_name='основное')),
                ('is_active', models.BooleanField(default=True, verbose_name='показывается')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maincatalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
