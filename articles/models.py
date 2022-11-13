from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')
    thumbnail = models.ImageField(upload_to='article-thumbnails', verbose_name='تصویر')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(verbose_name='متن کامنت')
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')
    related_article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله مربوطه')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
    
    def __str__(self):
        return f'{self.related_user}: {self.text}'

class Car(models.Model):
    title = models.CharField(max_length=64, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'خودرو'
        verbose_name_plural = 'خودروها'

    def __str__(self):
        return self.title