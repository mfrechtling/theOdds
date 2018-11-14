import requests
import json

def getApiKey():
    f = open("api.key", "r")
    key = f.readline().strip()
    return key

def getData(key, sport):
    parameters = {'apiKey': key, 'sport': sport, 'mkt': 'h2h', 'region': 'au'}
    response = requests.get("https://api.the-odds-api.com/v3/odds", params=parameters)
    return response.json()

def parseJsonData(data):
    for game in data["data"]:
        print(game["home_team"])
        for site in game["sites"]:
            print(site["site_key"])
            print(site["odds"]["h2h"][0])
            print(site["odds"]["h2h"][1])

def main():
    key = getApiKey()
    #results = getData(key, 'basketball_nba')
    f = open("results.json", "r")
    results = json.loads(f.read())
    parseJsonData(results)


if __name__ == '__main__':
    main() 
