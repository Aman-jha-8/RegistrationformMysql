from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    confirmPassword = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return self.name


class Regg(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    gender=models.CharField(max_length=7)
    college=models.CharField(max_length=15)

    def __str__(self):
        return self.name
