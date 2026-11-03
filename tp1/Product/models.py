from django.db import models

# Mes modèles.

class Category (models.Model) :
    cat_name= models.CharField(max_length=50)

class Ingredient(models.Model):
    ing_name=models.CharField(max_length=50)

class Product(models.Model):
    prd_name= models.CharField(max_length=50)
    price= models.FloatField(max_length=10)
    created_at= models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    ingredients=models.ManyToManyField(Ingredient, related_name="produits")
