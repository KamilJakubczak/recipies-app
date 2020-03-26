from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializers, IngridientSerializers
from .serializers import MealSerializers
from .models import Product, Ingridient, Meal
from rest_framework.response import Response
# Create your views here.

class IngridientViewSet(viewsets.ModelViewSet):
    serializer_class = IngridientSerializers
    queryset = Ingridient.objects.all()

class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializers
    queryset = Meal.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
