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

def writeCsvData(fileName, data):
    f = open(fileName, "w")
    f.write("home, away, home_odds, away_odds\n")
    for game in data["data"]:
        if (game["teams"][0] ==  game["home_team"]):
            home_index = 0
            away_index = 1
        else:
            home_index = 1
            away_index = 0
        for site in game["sites"]:
            if (site["site_key"] != "sportsbet"):
                continue
            f.write(game["teams"][home_index] + "," + game["teams"][away_index] + "," + str(site["odds"]["h2h"][home_index]) + "," + str(site["odds"]["h2h"][away_index]) + "\n")
    f.close()

def main():
    key = getApiKey()
    results = getData(key, 'basketball_nba')
    f = open("results.json", "w")
    f.write(json.dumps(results))
    f.close()
    f = open("results.json", "r")
    results = json.loads(f.read())
    writeCsvData("./results.csv", results)


if __name__ == '__main__':
    main() 
