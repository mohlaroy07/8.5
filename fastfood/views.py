from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category, Food, Order
from .serializers import CategorySerializer, FoodSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status



class CategoryView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                category = category.objects.get(pk=pk)
                return Response(CategorySerializer(category).data)
            except:
                return Response({"message": "Category Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
        categories = category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)
        
    
    def post(self, request):
        nomi = request.data["nomi"]
        category = category.objects.create(nomi=nomi)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    
    def delete(self, request):
        category = self.get_object()
        if category is None:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_404_NO_CONTENT)
    
    
    def put(self, request, pk=None):
        if not pk:
            return Response("Method PUT not allowed", status=status.HTTP_404_NOT_FOUND)
        
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_category = serializer.update(category, serializer.validated_data)
        
        return Response(CategorySerializer(updated_category).data)
    


class FoodView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                food = Food.objects.get(pk=pk)
                return Response(FoodSerializer(food).data)
            except:
                return Response({"message": "Food Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
        foods = Food.objects.all()
        return Response(FoodSerializer(foodny=True).data)
    
    
    def post(self, request):
        nomi = request.data["nomi"]
        description = request.data["description"]
        price = request.data["price"]
        ingredients = request.data["ingredients"]
        food = Food.objects.create(nomi=nomi, description=description, price=price, ingredients=ingredients)      
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    
    
    
    def delete(self, request):
        food = self.get_object()
        if food is None:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        food.delete()
        return Response(status=status.HTTP_404_NOT_CONTEND)
    
    
    def put(self, request, pk=None):
        if not pk:
            return Response("Method PUT not allowed", status=status.HTTP_404_NOT_FOUND)
        
        food = Food.objects.get(pk=pk)
        serializer = FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_food = serializer.update(food, serializer.validated_data)
        
        return Response(FoodSerializer(updated_food).data)
    
    
        
class OrderView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                order = Order.objects.get(pk=pk)
                return Response(OrderSerializer(order).data)
            except:
                return Response({"message": "Order Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
        orders = Order.objects.all()
        return Response(OrderSerializer(orders, many=True).data)
    
    
    def post(self, request):
        count = request.data["count"]
        created_at = request.data["created_at"]
        category_id = request.data["category_id"]
        
        category = Category.objects.get(pk=category_id)
        
        food_id = request.data["food_id"]
        
        food = Food.objects.get(pk=food_id)
        
        order = Order.objects.create(count=count, created_at=created_at, category=category, food=food, order=order)
        
        serializer = OrderSerializer(order)
        return Response(serializer.data)        
        
        
    def delete(self, request):
        order = self.get_object()
        if order is None :
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND) 
        order.delete()
        return Response(status=status.HTTP_404_NOT_CONTEND)
     
     
    def put(self, request, pk=None):
        if not pk:
            return Response("Method PUT not allowed", status=status.HTTP_404_NOT_FOUND)
        
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_order = serializer.update(order, serializer.validated_data)
        
        return Response(OrderSerializer(updated_order).data)