from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_num  = models.IntegerField()
    # produce_time = models.DateTimeField()
    # produce_time1= models.DateField()
    description  = models.TextField()
    pictures     = models.BooleanField()
    other_content= models.TextField()


