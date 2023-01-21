# Generated by Django 4.1.5 on 2023-01-21 15:10

from django.db import migrations, models
import django.db.models.deletion
import khanshop.enums


class Migration(migrations.Migration):

    dependencies = [
        ('maincatalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='имя продукта')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=300, verbose_name='краткое описание продукта')),
                ('description', models.TextField(blank=True, verbose_name='описание продукта')),
                ('price', models.DecimalField(decimal_places=0, default=None, max_digits=8, null=True, verbose_name='цена продукта')),
                ('quantity', models.PositiveIntegerField(default=0, null=True, verbose_name='количество на складе')),
                ('status', models.CharField(choices=[(khanshop.enums.StatusChoice['YES'], 'в наличии'), (khanshop.enums.StatusChoice['LIM'], 'количество ограничено'), (khanshop.enums.StatusChoice['END'], 'нет в наличии'), (khanshop.enums.StatusChoice['ASK'], 'под заказ'), (khanshop.enums.StatusChoice['DEL'], 'снято с производства')], max_length=100, verbose_name='тип')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maincatalog.category')),
            ],
        ),
    ]
