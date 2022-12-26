from django.contrib import admin

from core.models import Food, FoodCategory, Topping

admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(Topping)