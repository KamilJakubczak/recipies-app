from django.contrib import admin
from .models import Product, Ingridient, Meal, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Ingridient)
admin.site.register(Meal)
admin.site.register(Category)
