from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=244)
    
    def __str__(self) -> str:
        return self.name

    
    
class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    name = models.CharField(max_length=244)
    description = models.TextField()
    price = models.IntegerField()
    ingredients = models.CharField(max_length=244)
    
    def __str__(self) -> str:
        return self.name
    
    
  
class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self) -> str:
        return self.food