from rest_framework import serializers
from .models import Category, Food, Order



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        
        
class FoodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Food
        fields = '__all__'
        
                
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'        