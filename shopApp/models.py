from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Dnditem(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.FloatField()
    item_weight = models.CharField(max_length=200)
    shop_vendor = models.CharField(max_length=200)
    rarity = models.CharField(max_length=200)

class vendor(models.Model):
    items=models.ForeignKey(Dnditem,on_delete=models.CASCADE)
    

    