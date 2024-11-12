#!/usr/bin/python3
#Import required stuff to work with the API and the JSON responses.
import requests
from requests.auth import HTTPBasicAuth
import json

#Set IDS for Authentication

cid = "Client ID"
cs = "Client Secret"
org = "Org ID"

#Set the basic Headers
headers = {"Accept":"application/json;version=v1alpha","Organization":org}

#Get the token for authentication
tresponse = requests.post('https://app.nobl9.com/api/accessToken',
                              auth=HTTPBasicAuth(cid, cs),headers=headers)
#Process the json response and save the token
bearerjson = json.loads(tresponse.content)
bearertoken = bearerjson["access_token"]

#Add the token to the header
headers["Authorization"] = "Bearer "+bearertoken

#get the json response payload
getresponse = requests.get('https://app.nobl9.com/api/v1/slos', headers=headers)

print(getresponse.content)
