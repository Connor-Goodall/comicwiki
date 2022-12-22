from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import superheroPowerstats, superheroAppearance, superheroBiography, superheroWork, superheroConnections, superheroImages
import json
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def gettingAPI():
    superheroData = []
    for i in range(731):
        number = i + 1
        superhero = requests.get(f"https://akabab.github.io/superhero-api/api/id/{number}.json")
        if(superhero.status_code != 404):
            jsonSuperheroData = json.loads(superhero.text)
            superheroData.append(jsonSuperheroData)
    return superheroData


def characterInfo(request, name):
    characterImage = superheroImages.objects.filter(name = name)
    characterAppearance = superheroAppearance.objects.filter(name = name)
    characterWork = superheroWork.objects.filter(name = name)
    characterConnections = superheroConnections.objects.filter(name = name)
    characterBiography = superheroBiography.objects.filter(name = name)
    characterPowerstats = superheroPowerstats.objects.filter(name = name)
    return render(request, 'characterInfo.html', {'biography': characterBiography[0], 'image': characterImage[0],
                                                  'appearance': characterAppearance[0], 'work': characterWork[0],
                                                  'connections': characterConnections[0], 'powerstats': characterPowerstats[0]})
def createSuperhero():
    data = gettingAPI()
    for superhero in data:
        onePowerStats = superheroPowerstats(name = superhero["name"], intelligence = superhero["powerstats"]
        ["intelligence"], strength = superhero["powerstats"]["strength"], speed = superhero["powerstats"]["speed"],
                                            durability = superhero["powerstats"]["durability"], power = superhero
            ["powerstats"]["power"], combat = superhero["powerstats"]["combat"])
        if(superhero["appearance"]["race"] == None):
            race = "Unknown"
        else:
            race = superhero["appearance"]["race"]
        heightList = superhero["appearance"]["height"]
        height = ""
        for heightNumber in range(len(heightList)):
            height += heightList[heightNumber]
            if (heightNumber != len(heightList) - 1):
                height += " or "
        weightList = superhero["appearance"]["weight"]
        weight = ""
        for weightNumber in range(len(weightList)):
            weight += weightList[weightNumber]
            if (weightNumber != len(weightList) - 1):
                weight += " or "
        oneAppearance = superheroAppearance(name = superhero["name"], gender = superhero["appearance"]["gender"], race =
                                            race, height = height, weight = weight, eyeColor =
                                            superhero["appearance"]["eyeColor"], hairColor = superhero["appearance"]["hairColor"])
        aliasList = superhero["biography"]["aliases"]
        aliases = ""
        for aliasNumber in range(len(aliasList)):
            aliases += aliasList[aliasNumber]
            if (aliasNumber != len(aliasList) - 1):
                aliases += ", "
        if(superhero["biography"]["publisher"] == None):
            publisher = ""
        else:
            publisher = superhero["biography"]["publisher"]
        oneBiography = superheroBiography(name = superhero["name"], fullName = superhero["biography"]["fullName"],
                                          alterEgos = superhero["biography"]["alterEgos"], aliases = aliases,
                                          birthPlace = superhero["biography"]["placeOfBirth"], firstAppearance =
                                          superhero["biography"]["firstAppearance"], publisher = publisher, alignment = superhero["biography"]["alignment"])
        oneWork = superheroWork(name = superhero["name"], occupation = superhero["work"]["occupation"], base = superhero
                                ["work"]["base"])
        oneConnection = superheroConnections(name = superhero["name"], groupAffiliation = superhero["connections"]
        ["groupAffiliation"], relatives = superhero["connections"]["relatives"])
        oneImage = superheroImages(name = superhero["name"], small = superhero["images"]["sm"], medium = superhero["images"]
                                   ["md"], large = superhero["images"]["lg"])
        onePowerStats.save()
        oneAppearance.save()
        oneBiography.save()
        oneWork.save()
        oneConnection.save()
        oneImage.save()