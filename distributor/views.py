from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from distributor.models import Product, Category, Tag
from distributor.serializers import ProductSerializer, CategorySerializer, TagSerializer


class ListCreateProductAPI(APIView, PageNumberPagination):
    allowed_methods = ['get', 'post']

    def get(self, request):
        search = request.query_params.get('search', '')
        # category_id = request.query_params.get('category')
        products = Product.objects.filter(Q(title__icontains=search) |
                                          Q(text__icontains=search))
        results = self.paginate_queryset(products, request, view=self)
        data = ProductSerializer(results, many=True).data
        return self.get_paginated_response(data)

    def post(self, request):
        title = request.data.get('title')
        text = request.data.get('text')
        category_id = int(request.data.get('category_id'))
        product = Product.objects.create(title=title, text=text, category_id=category_id)
        product.save()
        return Response(status=status.HTTP_200_OK, data=ProductSerializer(product).data)


class ListCreateCategoryAPI(APIView, PageNumberPagination):
    allowed_methods = ['get', 'post']

    def get(self, request):
        search = request.query_params.get('search', '')
        categorys = Category.objects.filter(Q(title__icontains=search) |
                                            Q(text__icontains=search))
        results = self.paginate_queryset(categorys, request, view=self)
        data = CategorySerializer(results, many=True).data
        return self.get_paginated_response(data)

    def post(self, request):
        title = request.data.get('title')
        text = request.data.get('text')
        category = Category.objects.create(title=title, text=text)
        category.save()
        data = CategorySerializer(category).data
        return Response(status=status.HTTP_200_OK, data=data)


class ListCreateTagAPI(APIView, PageNumberPagination):
    allowed_methods = ['get', 'post']

    def get(self, request):
        search = request.query_params.get('search', '')
        tags = Tag.objects.filter(Q(title__icontains=search) |
                                  Q(text__icontains=search))
        results = self.paginate_queryset(tags, request, view=self)
        data = TagSerializer(results, many=True).data
        return self.get_paginated_response(data)

    def post(self, request):
        title = request.data.get('title')
        text = request.data.get('text')
        tag = Tag.objects.create(title=title, text=text)
        tag.save()
        data = TagSerializer(tag).data
        return Response(status=status.HTTP_200_OK, data=data)


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
        return Response(status=status.HTTP_200_OK, data=ProductSerializer(product).data)


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
