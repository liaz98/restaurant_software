from rest_framework import viewsets
from django_filters import rest_framework as filters
from api.serializers.food_category import FoodSerializer
from core.models import Food


class FoodView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('is_vegan', 'is_special', 'toppings__name')

