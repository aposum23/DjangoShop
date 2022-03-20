from django.contrib import admin
from shop_api.models import Categories, Salesman, Product, Photography

# Register your models here.
admin.site.register(Categories)
admin.site.register(Salesman)
admin.site.register(Product)
admin.site.register(Photography)
