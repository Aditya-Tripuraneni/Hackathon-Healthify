import requests
import os

TOKEN = os.environ.get("YELP_TOKEN")

endpoint = "https://api.yelp.com/v3/businesses/search"
header = {"Authorization": "Bearer " + TOKEN}


def get_data(type, location):
    paramaters_gym = {
        "term": type,
        "location": location,
        "limit": 10
    }
    request = requests.get(endpoint, headers=header, params=paramaters_gym)
    print(request.headers)
    json_data = request.json()["businesses"]
    string = ""
    for business in json_data:
        if not business["is_closed"]:
            data_string = f"""{business["name"]} on {business["location"]["address1"]}"""
            string += data_string + "\n"

    return string



