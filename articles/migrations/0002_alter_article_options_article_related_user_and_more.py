# Generated by Django 4.1.1 on 2022-10-23 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقاله ها'},
        ),
        migrations.AddField(
            model_name='article',
            name='related_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر مربوطه'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=64, verbose_name='عنوان'),
        ),
    ]