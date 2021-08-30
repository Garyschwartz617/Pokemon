import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pokemon.settings')
django.setup()

from card.models import *


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
            c.type.set(typs)

# print(Type.objects.all())
# for l in range(1,152):
#     create(l)        
