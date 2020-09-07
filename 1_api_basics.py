import requests
from pprint import pprint

url = "https://api.spacexdata.com/v4/launches/latest"

# Get http is what it sounds like, get something from the site
response = requests.get(url)

# Most APIs these days send back JSON
json_string = response.json()

# This just prints out the values
pprint(json_string)


# Get a SpaceX Launch
# https://github.com/r-spacex/SpaceX-API/blob/master/docs/v4/README.md
url = "https://api.spacexdata.com/v4/launches/5eb87cdeffd86e000604b330"
response = requests.get(url)
pprint(response.json())
