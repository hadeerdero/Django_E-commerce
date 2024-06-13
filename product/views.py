from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Categoty
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        # return Response(serializer.data)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class ProductDetails(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
           
            return Categoty.objects.get(slug=category_slug)
        except Categoty.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
