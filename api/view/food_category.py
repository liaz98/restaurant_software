from rest_framework import viewsets
from api.serializers import FoodCategorySerializer
from core.models import FoodCategory


class FoodCategoryView(viewsets.ModelViewSet):
    serializer_class = FoodCategorySerializer
    queryset = FoodCategory.objects.filter(is_publish=True)
