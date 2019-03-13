from django.db import models

# Create your models here.
class Product(models.Model):
    # product_name = models.CharField(max_length=30)
    # product_num  = models.IntegerField()
    # # produce_time = models.DateTimeField()
    # # produce_time1= models.DateField()
    # description  = models.TextField()
    # pictures     = models.BooleanField()
    # other_content= models.TextField()
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    summary = models.TextField(default='blank',blank=False,null=False)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f"/products/{self.id}/"

