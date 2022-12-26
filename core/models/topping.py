from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=150)
    food = models.ForeignKey('Food', on_delete=models.CASCADE, related_name='toppings')

    def __str__(self):
        return str(self.name)

