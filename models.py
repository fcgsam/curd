from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number= models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name 
    