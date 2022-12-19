import requests
import json
def gettingAPI():
    superheroData = []
    for i in range(731):
        number = i + 1
        superhero = requests.get(f"https://akabab.github.io/superhero-api/api/id/{number}.json")
        if(superhero.status_code != 404):
            jsonSuperheroData = json.loads(superhero.text)
            superheroData.append(jsonSuperheroData)
    return superheroData
data = gettingAPI()

