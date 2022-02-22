from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    message=models.CharField(max_length=600)


    def __str__(self):
        return self.email

class category(models.Model):
    cname=models.CharField(max_length=30)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()










