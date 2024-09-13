from django.db import models

# Create your models here.
class Product(models.Model):
    ProductID = models.IntegerField()
    name = models.TextField()
    category = models.TextField()
    class Meta:
        permissions = [('can_change_category', 'Can change category')]