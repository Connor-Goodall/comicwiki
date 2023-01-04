from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import superheroPowerstats, superheroAppearance, superheroBiography, superheroWork, superheroConnections, superheroImages
import json
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
from .forms import SuperheroBiographyForm, SuperheroAppearanceForm, SuperheroWorkForm, SuperheroConnectionsForm, SuperheroPowerstatsForm, SuperheroImagesForm, SuperheroNameForm, SuperheroCreationForm
# Create your views here.

def index(request):
    ironman = superheroImages.objects.filter(name = "Iron Man")
    spiderman = superheroImages.objects.filter(name = "Spider-Man")
    captain_america = superheroImages.objects.filter(name = "Captain America")
    batman = superheroImages.objects.filter(name = "Batman (Bruce Wayne)")
    superman = superheroImages.objects.filter(name = "Superman")
    wonderWoman = superheroImages.objects.filter(name = "Wonder Woman")
    darthVader = superheroImages.objects.filter(name = "Darth Vader")
    goku = superheroImages.objects.filter(name = "Goku")
    onePunchMan = superheroImages.objects.filter(name = "One Punch Man")
    return render(request, 'index.html', {'spiderman': spiderman[0], 'ironman': ironman[0], 'captain': captain_america[0],
                                          'batman': batman[0], 'superman': superman[0], 'wonderWoman': wonderWoman[0],
                                          'darthVader': darthVader[0], 'goku': goku[0], 'onePunchMan': onePunchMan[0]})

def gettingAPI():
    superheroData = []
    superheroDict = dict()
    for i in range(731):
        number = i + 1
        superhero = requests.get(f"https://akabab.github.io/superhero-api/api/id/{number}.json")
        if (superhero.status_code != 404):
            jsonSuperheroData = json.loads(superhero.text)
            if (jsonSuperheroData["biography"]["fullName"] == ""):
                jsonSuperheroData["biography"]["fullName"] = "Unknown"
            if ("III" in jsonSuperheroData["name"]):
                jsonSuperheroData["name"] = jsonSuperheroData["name"].replace("III", "(" +
                                                                              jsonSuperheroData["biography"]["fullName"]
                                                                              + ")")
            elif ("II" in jsonSuperheroData["name"]):
                jsonSuperheroData["name"] = jsonSuperheroData["name"].replace("II", "(" +
                                                                              jsonSuperheroData["biography"]["fullName"]
                                                                              + ")")
            elif (" IV" in jsonSuperheroData["name"]):
                jsonSuperheroData["name"] = jsonSuperheroData["name"].replace(" IV", " (" +
                                                                              jsonSuperheroData["biography"]["fullName"]
                                                                              + ")")
            elif ("VI" in jsonSuperheroData["name"]):
                jsonSuperheroData["name"] = jsonSuperheroData["name"].replace("VI", "(" +
                                                                              jsonSuperheroData["biography"]["fullName"]
                                                                              + ")")
            elif (" V" in jsonSuperheroData["name"] and "V" == jsonSuperheroData["name"][
                    len(jsonSuperheroData["name"]) - 1]):
                jsonSuperheroData["name"] = jsonSuperheroData["name"].replace(" V", " (" +
                                                                              jsonSuperheroData["biography"]["fullName"]
                                                                              + ")")
            if (jsonSuperheroData["name"] in superheroDict):
                superheroData[len(superheroData) - 1]["name"] = superheroData[len(superheroData) - 1]["name"] + " (" + \
                                               superheroData[len(superheroData) - 1]["biography"]["fullName"] + ")"
                jsonSuperheroData["name"] = jsonSuperheroData["name"] + " (" + jsonSuperheroData["biography"][
                    "fullName"] + ")"
            superheroDict[jsonSuperheroData["name"]] = True
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

def allCharacters(request):
    character_set = superheroBiography.objects.all().order_by("name")
    return render(request, 'allCharacters.html', {'characters': character_set})


def marvelCharacters(request):
    good_marvel_set = superheroBiography.objects.filter(publisher = "Marvel Comics", alignment = "good").order_by("name")
    neutral_marvel_set = superheroBiography.objects.filter(publisher="Marvel Comics", alignment="neutral").order_by("name")
    bad_marvel_set = superheroBiography.objects.filter(publisher = "Marvel Comics", alignment = "bad").order_by("name")
    return render(request, 'marvelCharacters.html', {'goodMarvelCharacters': good_marvel_set, 'neutralMarvelCharacters':
    neutral_marvel_set, 'badMarvelCharacters': bad_marvel_set})

def dcCharacters(request):
    good_dc_set = superheroBiography.objects.filter(publisher = "DC Comics", alignment = "good").order_by("name")
    bad_dc_set = superheroBiography.objects.filter(publisher = "DC Comics", alignment = "bad").order_by("name")
    return render(request, 'dcCharacters.html', {'goodDCCharacters': good_dc_set, 'badDCCharacters': bad_dc_set})

def otherCharacters(request):
    lucasfilm = superheroBiography.objects.filter(publisher = "George Lucas").order_by("name")
    startrek = superheroBiography.objects.filter(publisher = "Star Trek").order_by("name")
    manga = superheroBiography.objects.filter(publisher = "Shueisha").order_by("name")
    darkHorse = superheroBiography.objects.filter(publisher = "Dark Horse Comics").order_by("name")
    return render(request, 'otherCharacters.html', {'lucasfilmCharacters': lucasfilm, 'startrekCharacters': startrek,
                                                    'mangaCharacters': manga, 'darkHorseCharacters': darkHorse})
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

class SearchResultsView(ListView):
    model = superheroImages
    template_name ='searchResults.html'
    def get_queryset(self):
        query = self.request.GET.get("result")
        object_list = superheroImages.objects.filter(
            Q(name__contains=query)
        )
        return object_list

@login_required
def edit(request, name):
    biography = superheroBiography.objects.filter(name = name).first()
    appearance = superheroAppearance.objects.filter(name = name).first()
    work = superheroWork.objects.filter(name = name).first()
    connections = superheroConnections.objects.filter(name = name).first()
    powerstats = superheroPowerstats.objects.filter(name = name).first()
    image = superheroImages.objects.filter(name = name).first()
    if request.method == 'POST':
        sn_form = SuperheroNameForm(request.POST, instance = biography)
        sb_form = SuperheroBiographyForm(request.POST, instance = biography)
        sa_form = SuperheroAppearanceForm(request.POST, instance = appearance)
        sw_form = SuperheroWorkForm(request.POST, instance = work)
        sc_form = SuperheroConnectionsForm(request.POST, instance = connections)
        sp_form = SuperheroPowerstatsForm(request.POST, instance = powerstats)
        image_form = SuperheroImagesForm(request.POST, request.FILES, instance = image)
        if sb_form.is_valid() and sa_form.is_valid() and sw_form.is_valid() and sc_form.is_valid() and \
                sp_form.is_valid() and image_form.is_valid() and sn_form.is_valid():
            sb_form.save()
            sa_form.save()
            sw_form.save()
            sc_form.save()
            sp_form.save()
            image_form.save()
            sn_form.save()
            superheroAppearance.objects.filter(name=name).update(name=biography.name)
            superheroPowerstats.objects.filter(name=name).update(name=biography.name)
            superheroWork.objects.filter(name=name).update(name=biography.name)
            superheroConnections.objects.filter(name=name).update(name=biography.name)
            superheroImages.objects.filter(name=name).update(name=biography.name)
            return redirect(f"/comics/{biography.name}/")
    else:
        sn_form = SuperheroNameForm(instance = biography)
        sb_form = SuperheroBiographyForm(instance = biography)
        sa_form = SuperheroAppearanceForm(instance = appearance)
        sw_form = SuperheroWorkForm(instance = work)
        sc_form = SuperheroConnectionsForm(instance = connections)
        sp_form = SuperheroPowerstatsForm(instance = powerstats)
        image_form = SuperheroImagesForm(instance = image)
        return render(request, 'edit.html', {'sb_form': sb_form, 'sa_form': sa_form, 'sw_form': sw_form,
                                             'sc_form': sc_form, 'sp_form': sp_form, 'image_form': image_form,
                                             'sn_form': sn_form})

@login_required
def addCharacter(request):
    if request.method == 'POST':
        character = SuperheroCreationForm(request.POST)
        if character.is_valid():
            character.save()
            name = character.cleaned_data.get('name')
            characterAppearance = superheroAppearance(name = name, gender = "-", race = "-", height = "-",
                                                      weight = "-", eyeColor = "-", hairColor = "-")
            characterWork = superheroWork(name = name, occupation = "-", base = "-")
            characterConnections = superheroConnections(name = name, groupAffiliation = "-", relatives = "-")
            characterPowerstats = superheroPowerstats(name = name, intelligence = 0, strength = 0, speed = 0,
                                                      durability = 0, power = 0, combat = 0)
            characterImages = superheroImages(name = name,
            small = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/sm/no-portrait.jpg",
            medium = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/md/no-portrait.jpg",
            large = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/no-portrait.jpg")
            characterAppearance.save()
            characterWork.save()
            characterConnections.save()
            characterPowerstats.save()
            characterImages.save()
            return redirect('/comics/allcharacters')
    else:
        character = SuperheroCreationForm()
        return render(request, 'addCharacter.html', {'character': character})