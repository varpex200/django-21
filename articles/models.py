from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
    
    def __str__(self):
        return self.title
