from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class LatestProductList(APIView):
    def get(self,request, format=None):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        # return Response(serializer.data)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        
