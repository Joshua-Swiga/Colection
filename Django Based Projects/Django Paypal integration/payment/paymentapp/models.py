from django.db import models

# Create your models here.
class Product(models.Model):
    product_image = models.URLField(blank= True, null= True)
    product_name = models.CharField(max_length=100, blank= True, null= True)
    product_price = models.IntegerField(blank= True, null= True)
    product_description = models.TextField()

    def __str__(self) -> str:
        return f'{self.product_name}: {self.product_description}'
