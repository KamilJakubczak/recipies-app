from django.db import models

# Create your models here.
#
class Product(models.Model):
    name = models.CharField(max_length=255)
    proteins = models.DecimalField(max_digits=7, decimal_places=2)
    carbohudrate = models.DecimalField(max_digits=7, decimal_places=2)
    fat = models.DecimalField(max_digits=7, decimal_places=2)


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

    def __str__(self):
       return self.description

class Meal(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingridients = models.ManyToManyField(Ingridient)
    
    def __str__(self):
        return self.name
