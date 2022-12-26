from rest_framework import serializers

from api.serializers import ToppingSerializer
from core.models import FoodCategory, Food


class FoodSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True, read_only=True)
    description = serializers.CharField()

    class Meta:
        model = Food
        fields = [
            'name',
            'description',
            'price',
            'is_vegan',
            'is_special',
            'toppings'
        ]


class FoodCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = [
            'id',
            'name',
            'foods'
        ]
