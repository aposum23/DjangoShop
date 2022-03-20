from django.db import models


class Categories(models.Model):
    cat_name = models.TextField(max_length=50)


class Salesman(models.Model):
    name = models.TextField(max_length=50)


class Product(models.Model):
    prod_name = models.TextField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)
    cost = models.FloatField(max_length=100)


class Photography(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_first = models.BooleanField()
    photo = models.ImageField(upload_to='product-images/')
