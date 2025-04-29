from django.db import models

# Create your models here.


class vacancy(models.Model):
    role=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    learn=models.CharField(max_length=100)
    vac=models.CharField(max_length=10,default="Not Mansion")

    def __str__(self):
        return self.company

class berojgar(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    skill=models.CharField(max_length=100)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.name



class application(models.Model):
    company = models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone=models.IntegerField()
    qualification=models.CharField(max_length=100)
    photo=models.FileField(upload_to="image",blank=True)
    apply = models.CharField(max_length=100,default='apply')

    def __str__(self):
        return self.name




class hrgroup(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    company=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name











