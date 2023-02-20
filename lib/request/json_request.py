import requests
import json

def json_request(json_url,headers={}):
    json = requests.get(json_url,headers=headers)
    return json