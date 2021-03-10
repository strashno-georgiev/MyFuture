from django.db import models

# Create your models here.
class Profession(models.Model):
    name = models.CharField(max_length=40)
    short_desc = models.CharField(max_length=500)
    long_desc = models.TextField(max_length=None)
    tags = models.CharField(max_length=65)
    def __str__(self):
        return self.name

class PersonalityType(models.Model):
    code = models.CharField(max_length=4)
    desc = models.TextField(max_length=None)
    def __str__(self):
        return self.code