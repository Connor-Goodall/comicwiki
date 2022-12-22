import requests
import json
def gettingAPI():
    superhero = requests.get(f"https://akabab.github.io/superhero-api/api/id/70.json")
    if(superhero.status_code != 404):
        jsonSuperheroData = json.loads(superhero.text)
    return jsonSuperheroData
data = gettingAPI()
name = data["name"]
intelligence = data["powerstats"]["intelligence"]
strength = data["powerstats"]["strength"]
speed = data["powerstats"]["speed"]
durability = data["powerstats"]["durability"]
power = data["powerstats"]["power"]
combat = data["powerstats"]["combat"]
gender = data["appearance"]["gender"]
race = data["appearance"]["race"]
heightList = data["appearance"]["height"]
height = ""
for heightNumber in range(len(heightList)):
    height += heightList[heightNumber]
    if(heightNumber != len(heightList) - 1):
        height += " or "
weightList = data["appearance"]["weight"]
weight = ""
for weightNumber in range(len(weightList)):
    weight += weightList[weightNumber]
    if(weightNumber != len(weightList) - 1):
        weight += " or "
eyeColor = data["appearance"]["eyeColor"]
hairColor = data["appearance"]["hairColor"]
fullName = data["biography"]["fullName"]
alterEgos = data["biography"]["alterEgos"]
aliasList = data["biography"]["aliases"]
aliases = ""
for aliasNumber in range(len(aliasList)):
    aliases += aliasList[aliasNumber]
    if(aliasNumber != len(aliasList) - 1):
        aliases += ", "
placeOfBirth = data["biography"]["placeOfBirth"]
firstAppearance = data["biography"]["firstAppearance"]
publisher = data["biography"]["publisher"]
alignment = data["biography"]["alignment"]
occupation = data["work"]["occupation"]
base = data["work"]["base"]
groupAffiliation = data["connections"]["groupAffiliation"]
relatives = data["connections"]["relatives"]
small_picture = data["images"]["sm"]
medium_picture = data["images"]["md"]
large_picture = data["images"]['lg']
print(large_picture)
print(data)
