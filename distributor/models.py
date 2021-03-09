from django.db import models

# Create your models here.
from django.db.models import SET_NULL


class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    title = models.CharField(max_length=100, verbose_name='Тег')
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def __str__(self):
        return str(self.title)

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=100, verbose_name='Категория')
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    is_active = models.BooleanField(default=False, verbose_name='Опубликован?')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def __str__(self):
        return str(self.title)

class ProductImage(models.Model):
    url = models.URLField(null=True)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)
