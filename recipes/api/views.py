from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializers, IngridientSerializers
from .models import Product, Ingridient
from rest_framework.response import Response
# Create your views here.

class IngridientViewSet(viewsets.ModelViewSet):
    serializer_class = IngridientSerializers
    queryset = Ingridient.objects.all()
