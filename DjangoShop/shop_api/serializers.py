from rest_framework import serializers
from shop_api.models import Categories, Salesman, Product, Photography


class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ProductSerialize(serializers.ModelSerializer):
    category = CategoriesSerializer()
    salesman = SalesmanSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class PhotographySerializer(serializers.ModelSerializer):
    product = ProductSerialize()

    class Meta:
        model = Photography
        fields = '__all__'
