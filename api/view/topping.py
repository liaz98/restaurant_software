from rest_framework import viewsets
from api.serializers import ToppingSerializer
from core.models import Topping


class ToppingView(viewsets.ModelViewSet):
    serializer_class = ToppingSerializer
    queryset = Topping.objects.all()