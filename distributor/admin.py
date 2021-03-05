from django.contrib import admin

# Register your models here.
from distributor.models import Tag, Category, Product

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)