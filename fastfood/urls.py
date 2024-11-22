from django.urls import path
from .views import CategoryView, FoodView, OrderView


urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("food/", FoodView.as_view()),
    path("food/<int:pk>/", FoodView.as_view()),
    path("order/", OrderView.as_view()),
]