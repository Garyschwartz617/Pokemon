from django.db import models
from django.db.models.fields import CharField
import random
# Create your models here.
class Type(models.Model):
    species = models.CharField(max_length=100)
    def __str__(self):
        return self.species



class Card(models.Model):
    name = models.CharField(max_length=100)
    tipe = models.ManyToManyField(Type,blank=True)
    rarity = models.IntegerField()

    def create_cards(self):
        cards = Card.objects.all()
        for l in range(1,61):
            Singular.objects.create(card= random.choice(cards), owner = self.profile)

class Singular(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,related_name='deck') 

    # def __str__(self):
    #     return self.card.name
   


class Post(models.Model):
    singular = models.ForeignKey(Singular, on_delete=models.CASCADE)
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)


class Response(models.Model):
    STATUS_CHOICE = [
        ('O', 'Open'),
        ('C', 'Closed'),
    ]

    card_buyer = models.ForeignKey(Singular, on_delete=models.CASCADE)
    buyer = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=50, default='O') 


class Answer(models.Model):
    STATUS_CHOICE = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]
    transaction = models.OneToOneField(Response,on_delete=models.CASCADE)   
    accept = models.BooleanField()
    status = models.CharField(choices=STATUS_CHOICE, max_length=50, default='O') 

    def swap(self):
        if self.accept == True:
            owner_card = self.transaction.post.singular
            owner = self.transaction.post.profile
            buyer_card = self.transaction.buyer_card
            buyer = self.transaction.buyer
            owner_card.owner =buyer
            buyer_card.owner = owner
            owner_card.save()
            buyer_card.save()
            self.status = 'A'
            self.transaction.status = 'C'
        else:
            self.status = 'R' 
