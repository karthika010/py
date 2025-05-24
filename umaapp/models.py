from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
     return self.name

class Biodata(models.Model):
    studentname=models.CharField(max_length=50,null=True,blank=True)
    rollno=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=100)

    def __str__(self):
     return self.name
