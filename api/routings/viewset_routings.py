from rest_framework import routers
from api.view import FoodView, ToppingView, FoodCategoryView

router = routers.SimpleRouter()
router.register("food", FoodView)
router.register("food-category", FoodCategoryView)
router.register("topping", ToppingView)



