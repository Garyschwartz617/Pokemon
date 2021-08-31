from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Person(models.Model):
    evil_scale = models.IntegerField()
    tipe = models.CharField(max_length= 50)
    strength = models.IntegerField()
    def __str__(self):
        return self.tipe


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=30, null=True)
    person = models.ForeignKey(Person,on_delete=CASCADE, null=True)

    def __str__(self):
        return self.user.username
