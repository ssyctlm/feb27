from django.db import models


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length = 30),
    company = models.CharField(max_length = 30),

    phone_number = models.CharField(max_length = 11),
    require = models.TextField()
