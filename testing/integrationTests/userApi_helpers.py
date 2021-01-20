import requests
import json

def getUsers(url):
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response

def createUser(url, firstname, lastname, age, address):
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
        "address": address
    }
    payload = json.dumps(data)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def deleteUser(url):
    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response

def updateUser(url, firstname, lastname, age, address):
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
        "address": address
    }
    payload = json.dumps(data)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response