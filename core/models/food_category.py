from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=150)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
