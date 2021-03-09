from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from distributor.models import Product, Category, Tag
from distributor.serializers import ProductSerializer, CategorySerializer, TagSerializer


@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        text = request.data.get('text')
        category_id = int(request.data.get('category_id'))
        product = Product.objects.create(title=title, text=text, category_id=category_id)
        product.save()
        return Response(status=status.HTTP_200_OK, data=ProductSerializer(product).data )

@api_view(['GET', 'POST'])
def category_list_view(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        data = CategorySerializer(categorys, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        text = request.data.get('text')
        category = Category.objects.create(title=title, text=text)
        category.save()
        return Response(status=status.HTTP_200_OK, data=CategorySerializer(category).data)

@api_view(['GET', 'POST'])
def tag_list_view(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        data = TagSerializer(tags, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        text = request.data.get('text')
        tag = Tag.objects.create(title=title, text=text)
        tag.save()
        return Response(status=status.HTTP_200_OK, data=TagSerializer(tag).data)