from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    phone=models.IntegerField()
    college=models.CharField(max_length=20)
    hobbies=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
