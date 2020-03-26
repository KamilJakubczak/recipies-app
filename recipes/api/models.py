from django.db import models
from django.db.models import DecimalField, F

# Create your models here.
#
class Product(models.Model):
    name = models.CharField(max_length=255)
    proteins = models.DecimalField(max_digits=7, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=7, decimal_places=2)
    fat = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Ingridient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    grams = models.IntegerField(blank=True, null=True)
    pieces = models.IntegerField(blank=True, null=True)
    milimiters = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255)

    @property
    def kcal(self):
        return round((self.product.proteins * 4 \
                     + self.product.carbohydrates * 4 \
                     + self.product.fat * 9)/100 * self.grams, 2)

    def __str__(self):
        return self.description

class Meal(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingridients = models.ManyToManyField(Ingridient)

    @property
    def total_proteins(self):
        total_proteins = 0
        for ingrident in self.ingridients.all():
            total_proteins += ingrident.product.proteins \
                              * ingrident.grams/100
        return round(total_proteins, 2)

    @property
    def total_carbohydrates(self):
        total_carbohydrates = 0
        for ingrident in self.ingridients.all():
            total_carbohydrates += ingrident.product.carbohydrates \
                                   * ingrident.grams/100
        return round(total_carbohydrates, 2)

    @property
    def total_fat(self):
        total_fat= 0
        for ingrident in self.ingridients.all():
            total_fat += ingrident.product.fat*ingrident.grams/100
        return round(total_fat, 2)

    @property
    def total_kcal(self):
        """Returns all the kalories for the particulat meal"""
        return round(self.total_proteins * 4 \
                     + self.total_carbohydrates * 4 \
                     + self.total_fat * 9, 2)

    def __str__(self):
        return self.name


