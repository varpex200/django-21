# Generated by Django 4.1.2 on 2022-11-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(upload_to='article-thumbnails', verbose_name='تصویر'),
        ),
    ]
