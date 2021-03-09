from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from distributor.models import Tag, Category, Product, ProductImage


class ImageProduct(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="height:100px" />'.format(obj.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ['image_tag',]


class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = 'id title text category is_active created updated'.split()
    readonly_fields = 'created updated'.split()
    search_fields = 'title text'.split()
    list_filter = 'updated category'.split()
    inlines = [ImageInline]


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(ProductImage, ImageProduct)
admin.site.register(Product, ProductAdmin)
