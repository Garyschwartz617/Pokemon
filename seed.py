import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pokemon.settings')
django.setup()

from card.models import *
from accounts.models import *


import requests
def get_info(num):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{num}')
    if response.status_code == 200:
        data = response.json()
        print (data['id'])
        print (data['name'])
        print (data['types'][0]['type']['name'])
        # print(data['species']['url'])
        rarity = data['species']['url']
        response = requests.get(rarity)
        if response.status_code == 200:
            species = response.json()
            print(species['capture_rate'])

# for l in range(1,350):
#     get_info(l)        

def create(num):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{num}')
    if response.status_code == 200:
        data = response.json()
        poke_name = data['name']
        typs = []
        for l in data['types']:
            nm = l['type']['name']
            x, t = Type.objects.get_or_create(species= nm)
            # if  not Type.objects.filter(species = nm).exists():
            #     Type.objects.create(species = nm)
            # x = Type.objects.get(species = nm) 
            typs.append(x)     
        rare = data['species']['url']
        response = requests.get(rare)
        if response.status_code == 200:
            r = response.json()['capture_rate']
            c =Card.objects.create(name = poke_name,rarity= r)
            c.tipe.set(typs)

# print(Type.objects.all())
# for l in range(1,150):
#     create(l)        
# Person.objects.create(evil_scale = 3, tipe = 'Nurse',strength = 5)
# Person.objects.create(evil_scale = 10, tipe = 'Team Rocket',strength = 6)
# Person.objects.create(evil_scale = 1, tipe = 'Ash',strength = 10)
# Person.objects.create(evil_scale = 8, tipe = 'Gary',strength = 9)
# Person.objects.create(evil_scale = 4, tipe = 'Gym Leader',strength = 8)
# Person.objects.create(evil_scale = 5, tipe = 'Elite 4',strength = 7)


# response = requests.get(f'https://archives.bulbagarden.net/wiki/Category:Bulbasaur')
# if response.status_code == 200:
#     data = response.json()
#     print (data)


# response = requests.get(f'https://pokeapi.co/api/v2/pokemon/898')
# if response.status_code == 200:
#     data = response.json()
#     poke_name = data['name']
#     print(poke_name)

from bs4 import BeautifulSoup

# page = requests.get("https://archives.bulbagarden.net/wiki/Category:Bulbasaur")

# soup = BeautifulSoup(page.content, 'html.parser')

# q =soup.find_all('img',decoding="async")
# a =q[0]['src']
# print(a)
# print(soup.prettify())
# bulb = Card.objects.get(id = 1)
# bulb.image = 'https://archives.bulbagarden.net/media/upload/thumb/0/09/001_Bulbasaur_Channel_2.png/120px-001_Bulbasaur_Channel_2.png'
# bulb.image = 'https://archives.bulbagarden.net/media/upload/thumb/8/8b/001Bulbasaur_Battle_Royale.jpg/240px-001Bulbasaur_Battle_Royale.jpg '
# bulb.image = 'https://archives.bulbagarden.net/media/upload/thumb/0/09/001_Bulbasaur_Channel_2.png/120px-001_Bulbasaur_Channel_2.png'
# bulb.save() 


# def get_image():
#     pokemon = Card.objects.all().filter(id__gt = 29,id__lt = 32)
#     for poke in pokemon:
#         p = poke.name
#         page = requests.get(f"https://archives.bulbagarden.net/wiki/Category:{p}")
#         soup = BeautifulSoup(page.content, 'html.parser')
#         q =soup.find_all('img',decoding="async")
#         a =q[0]['src']
#         b = f'{a}'
#         poke.image = b
#         poke.save() 

# # get_image()
# # farfetch'd, :Mr._Mime, Nidoran♀, Nidoran♂
# # farfetchd,mr-mime,nidoran-f,nidoran-m
# pokemon = Card.objects.get(name = 'nidoran-m')
# page = requests.get(f"https://archives.bulbagarden.net/wiki/Category:Nidoran♂")
# soup = BeautifulSoup(page.content, 'html.parser')
# q =soup.find_all('img',decoding="async")
# a =q[0]['src']
# b = f'{a}'
# pokemon.image = b
# pokemon.save()