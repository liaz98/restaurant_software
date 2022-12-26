from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    category_id = models.ForeignKey(
        'FoodCategory',
        on_delete=models.CASCADE,
        related_name='foods',
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.name)
