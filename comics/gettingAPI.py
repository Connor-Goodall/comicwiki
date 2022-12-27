import requests
import json
superheroDict = dict()
def gettingAPI():
    superheroData = []
    for i in range(6):
        number = i + 208
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
            elif (" V" in jsonSuperheroData["name"] and "V" == jsonSuperheroData["name"][len(jsonSuperheroData["name"]) - 1]):
                jsonSuperheroData["name"] = jsonSuperheroData["name"].replace(" V", " (" +
                                                                              jsonSuperheroData["biography"]["fullName"]
                                                                              + ")")
            if(jsonSuperheroData["name"] in superheroDict):
                superheroData[len(superheroData) - 1]["name"] = superheroData[len(superheroData) - 1]["name"] + " (" + \
                                               superheroData[len(superheroData)-1]["biography"]["fullName"] + ")"
                jsonSuperheroData["name"] = jsonSuperheroData["name"] + " (" + jsonSuperheroData["biography"]["fullName"] \
                                            + ")"
            superheroDict[jsonSuperheroData["name"]] = True
            superheroData.append(jsonSuperheroData)
    return superheroData
data = gettingAPI()
print(data)

