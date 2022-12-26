from rest_framework import serializers

from core.models import Topping


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['name']