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

# from bs4 import BeautifulSoup

# page = requests.get("https://archives.bulbagarden.net/wiki/Category:Bulbasaur")

# soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
bulb = Card.objects.get(id = 1)
# bulb.image = 'https://archives.bulbagarden.net/media/upload/thumb/0/09/001_Bulbasaur_Channel_2.png/120px-001_Bulbasaur_Channel_2.png" srcset="https://archives.bulbagarden.net/media/upload/thumb/0/09/001_Bulbasaur_Channel_2.png/180px-001_Bulbasaur_Channel_2.png 1.5x, https://archives.bulbagarden.net/media/upload/0/09/001_Bulbasaur_Channel_2.png 2x'
bulb.image = 'https://archives.bulbagarden.net/media/upload/thumb/8/8b/001Bulbasaur_Battle_Royale.jpg/240px-001Bulbasaur_Battle_Royale.jpg '
bulb.image = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fc%2Fc0%2FHarry_Potter_and_the_Chamber_of_Secrets_movie.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHarry_Potter_and_the_Chamber_of_Secrets_(film)&tbnid=g0A5dL9hy77P6M&vet=12ahUKEwjA067qg9zyAhVIYxoKHZKKAzUQMygBegUIARD-AQ..i&docid=LCXJEUuIn28w0M&w=368&h=270&q=harry%20potter%202&client=safari&ved=2ahUKEwjA067qg9zyAhVIYxoKHZKKAzUQMygBegUIARD-AQ'
bulb.save() 