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

class ProfessionEvent(models.Model):
    title = models.CharField(max_length=80)
    place = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)
    actual_date = models.DateTimeField()
    desc = models.TextField(max_length=None)
    profession = models.ForeignKey("Carriers.Profession", on_delete=models.CASCADE)
    def __str__(self):
        return self.title + "[{0}]".format(self.profession) 