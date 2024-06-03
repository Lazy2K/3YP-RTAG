import requests
import overpass

DEV_BASE = "https://master.apis.dev.openstreetmap.org"
VERSION_ENDPOINT = "/api/versions.json"

TEST_POINT = "www.overpass-api.de/api/xapi?*[maxspeed=*][bbox=5.6283473,50.5348043,5.6285261,50.534884]"

BOX_POINT = "/api/0.6/map?bbox="

S_POINT = "xapi?*[maxspeed=*][bbox=5.6283473,50.5348043,5.6285261,50.534884]"


TOP = 52.639
BOTTOM = 52.63
LEFT = 1.27
RIGHT = 1.279


# print(y.text)
#
"""


res = api.get('node["name"="Salt Lake City"]', responseformat="xml")

print(res)

mq = overpass.MapQuery(LEFT, BOTTOM, RIGHT, TOP)
res2 = api.get(mq)

print(res2)

"""
####


api = overpass.API(timeout=1000)
response = api.get(
    'way["highway"](around:10, 52.634998, 1.271750);(._;>;);out;')

for feature in response.features:
    if feature.properties:
        print(feature.properties)
        if 'highway' in feature.properties:
            print(feature.properties["maxspeed"])
