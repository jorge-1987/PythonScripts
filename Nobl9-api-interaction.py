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
tokenresponse = requests.post('https://app.nobl9.com/api/accessToken',
                              auth=HTTPBasicAuth(cid, cs),headers=headers)
