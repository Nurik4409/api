from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=255),
    decription = models.CharField(max_length=100),
    price = models.BigIntegerField(),
    in_stock = models.CharField(max_length=255)

    def __str__(self):
        return self.name    