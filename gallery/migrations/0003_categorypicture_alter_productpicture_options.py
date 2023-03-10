# Generated by Django 4.1.5 on 2023-03-05 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maincatalog', '0015_alter_category_urlname_alter_product_price_and_more'),
        ('gallery', '0002_alter_productpicture_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPicture',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='get_images', serialize=False, to='maincatalog.category', verbose_name='продукт')),
                ('short_desc', models.TextField(blank=True, max_length=50, verbose_name='описание')),
                ('image', models.ImageField(blank=True, upload_to='uploads/category/', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Изображение категорий',
                'verbose_name_plural': 'Изображение категорий',
            },
        ),
        migrations.AlterModelOptions(
            name='productpicture',
            options={'verbose_name': 'Изображения продуктов', 'verbose_name_plural': 'Изображения продуктов'},
        ),
    ]
