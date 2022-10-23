from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
    
    def __str__(self):
        return self.title
