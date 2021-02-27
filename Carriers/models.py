from django.db import models

# Create your models here.
class Profession(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    tags = models.CharField(max_length=65)
    def __str__(self):
        return self.name