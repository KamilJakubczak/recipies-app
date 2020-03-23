from rest_framework import serializers
from .models import Product, Ingridient

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class IngridientSerializers(serializers.ModelSerializer):

    product = ProductSerializers(many=False)

    class Meta:
        model = Ingridient
        fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        ingrident = Ingridient.objects.create(**validated_data)
        for product_data in products_data:
            Product.objects.create(ingrident=ingrident, **product_data)
        return ingrident
