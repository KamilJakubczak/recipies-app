from django.urls import path, include
from . import views
from rest_framework import routers
from .views import IngridientViewSet, MealViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('ingridient', IngridientViewSet)
router.register('meal', MealViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
