from rest_framework import serializers
from .models import Product, Ingridient, Meal

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class IngridientSerializers(serializers.ModelSerializer):

    product = ProductSerializers(many=False)
    kcal = serializers.ReadOnlyField()

    class Meta:
        model = Ingridient
        fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('product')
        ingrident = Ingridient.objects.create(**validated_data)

        for product_data in products_data:
            Product.objects.create(ingrident=ingrident, **product_data)
        return ingrident

class MealSerializers(serializers.ModelSerializer):
    ingridients = IngridientSerializers(many=True)

    class Meta:
        model = Meal
        fields = '__all__'

    def create(self, validated_data):
        ingridients_data = validated_data.pop('ingridients')
        meal = Meal.objects.create(**validated_data)
        for ingridient_data in ingridients_data:
            Ingridient.objects.create(meal=meal, **ingridient_data)
        return meal
