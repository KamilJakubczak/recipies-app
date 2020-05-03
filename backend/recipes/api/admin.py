from django.contrib import admin
from .models import Product, Ingridient, Meal, Category

# Register your models here.
admin.site.register(Product)
@admin.register(Ingridient)
class IngridientAdmin(admin.ModelAdmin):
    list_display = ['description', 'kcal']
# admin.site.register(Ingridient)
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_kcal', 'total_proteins', 'total_carbohydrates',
                    'total_fat']
admin.site.register(Category)
