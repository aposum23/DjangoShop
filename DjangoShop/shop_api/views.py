from models import Product, Salesman, Categories, Photography
from serializers import SalesmanSerializer, CategoriesSerializer, ProductSerialize, PhotographySerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialize


class SalesmanList(generics.ListAPIView):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer


class CategoryList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProductFilter(APIView):
    def post(self, request, format=None):
        products = Product.objects.filter(request.data)
        serializer = ProductSerialize(data=products, many=True)
        return Response(serializer.data)


class PhotographyList(APIView):
    def post(self, request, format=None):
        photography = Photography.objects.filter(request.data)
        serializer = PhotographySerializer(data=photography, many=True)
        return Response(serializer.data)
