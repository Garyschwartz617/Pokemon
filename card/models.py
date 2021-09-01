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
    image = models.ImageField(upload_to='posts/', null=True,blank=True)   

    def create_cards(self):
        
        cards = Card.objects.all()
        card_collection = {

            2 : cards.filter(rarity__lte = 10),
            4 : cards.filter(rarity__gt = 10, rarity__lte = 50),
            5 : cards.filter(rarity__gt = 50, rarity__lte = 100),
            6 : cards.filter(rarity__gt = 100, rarity__lte = 200),
            7 : cards.filter(rarity__gt = 200),
        }
        lst = []
        for key, value in card_collection.items():
            for l in range(1,key):
                sing = Singular(card= random.choice(value), owner = self.profile)
                lst.append(sing)
        Singular.objects.bulk_create(lst)
        BalanceUpdate.objects.create(profile = self.profile, amount = 500)

                # Singular(card= random.choice(value), owner = self.profile)
        # spr = cards.filter(rarity__lte = 50)
        # mdm = cards.filter(rarity__gt = 50, rarity__lte = 100)
        # potential = []
        # bd = []
        # for card in cards:
        #     if card.rarity <= 50:
        #         spr.append(card)
        #     elif card.rarity <= 100:
        #         mdm.append(card)
        #     elif card.rarity <= 200:
        #         potential.append(card)
        #     else:
        #         bd.append(card)
        # for l in range(1,3):
        #     Singular.objects.create(card= random.choice(spr), owner = self.profile)
        # for l in range(1,6):
        #     Singular.objects.create(card= random.choice(mdm), owner = self.profile)
        # for l in range(1,8):
        #     Singular.objects.create(card= random.choice(potential), owner = self.profile)
        # for l in range(1,11):
        #     Singular.objects.create(card= random.choice(bd), owner = self.profile)

        # for l in range(1,61):
        #     Singular.objects.create(card= random.choice(cards), owner = self.profile)

class Singular(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,related_name='deck') 

    def __str__(self):
        return self.card.name
   
class BalanceUpdate(models.Model):
    amount = models.IntegerField()
    profile = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,related_name='amount') 


class Post(models.Model):
    STATUS_CHOICE = [
        ('O', 'Open'),
        ('C', 'Closed'),
    ]
    singular = models.ForeignKey(Singular, on_delete=models.CASCADE)
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=50, default='O') 


class Response(models.Model):
    STATUS_CHOICE = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]

    card_buyer = models.ForeignKey(Singular, on_delete=models.CASCADE, null=True, blank = True)
    amount = models.IntegerField(null=True, blank = True)
    buyer = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=50, default='P') 
    def good(self):
        if self.amount == None:
            return True
        else: 
            transactions = BalanceUpdate.objects.filter(profile = self.buyer)
            money = 0
            for transaction in transactions:
                money += transaction.amount
            # print(money)
            if self.amount > money:
                return False
            else:
                return True   


class Answer(models.Model):
    
    transaction = models.OneToOneField(Response,on_delete=models.CASCADE)   
    accept = models.BooleanField()
    # status = models.CharField(choices=STATUS_CHOICE, max_length=50, default='P') 
    
    
    # def good(self):
    #     print(self)
    #     if self.transaction.amount == None:
    #         return True
    #     else:    
    #         transactions = BalanceUpdate.objects.filter(profile = self.transaction.buyer)
    #         money = 0
            
    #         for transaction in transactions:
    #             money += transaction.amount
    #         print(money)
    #         if self.transaction.amount > money:
    #             return False
    #         else:
    #             return True   

    def swap(self):
        if self.accept == True :
            if self.transaction.amount == None:
                owner_card = self.transaction.post.singular
                owner = self.transaction.post.profile
                buyer_card = self.transaction.card_buyer
                buyer = self.transaction.buyer
                owner_card.owner =buyer
                buyer_card.owner = owner
                owner_card.save()
                buyer_card.save()
                self.transaction.post.status = 'C'
                self.transaction.post.save()
                self.transaction.status = 'A'
                self.transaction.save()
            if self.transaction.card_buyer == None:
                owner_card = self.transaction.post.singular
                total = self.transaction.amount 
                buyer = self.transaction.buyer
                owner = self.transaction.post.profile
                loss = total - total - total
                BalanceUpdate.objects.create(profile = owner, amount = total)
                BalanceUpdate.objects.create(profile = buyer, amount = loss)
                owner_card.owner =buyer
                owner_card.save()
                self.transaction.post.status = 'C'
                self.transaction.post.save()
                self.transaction.status = 'A'
                self.transaction.save()
            else:
                total = self.transaction.amount 
                loss = total - total - total
                owner_card = self.transaction.post.singular
                owner = self.transaction.post.profile
                buyer_card = self.transaction.card_buyer
                buyer = self.transaction.buyer
                owner_card.owner =buyer
                buyer_card.owner = owner
                owner_card.save()
                buyer_card.save()
                BalanceUpdate.objects.create(profile = owner, amount = total)
                BalanceUpdate.objects.create(profile = buyer, amount = loss)


                self.transaction.post.status = 'C'
                self.transaction.post.save()
                self.transaction.status = 'A'
                self.transaction.save()
        else:
            self.transaction.status = 'R' 
            self.transaction.save()
