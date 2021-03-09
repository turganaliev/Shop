from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from distributor.models import Product
from distributor.serializers import ProductSerializer


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