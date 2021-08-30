from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Thread(models.Model):
    subject = models.CharField(max_length=200)
    creator = models.ForeignKey('accounts.Profile', on_delete=CASCADE)
    created = models.TimeField(auto_now_add=True)

class Comment(models.Model):
    thread = models.ForeignKey(Thread,on_delete=CASCADE)
    text = models.TextField()
    user_id = models.ForeignKey('accounts.Profile', on_delete=CASCADE)
    created = models.TimeField(auto_now_add=True)