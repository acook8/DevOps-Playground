import pytest
import requests
# def test_file1_method1():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"
# 	assert x == y,"test failed"
# def test_file1_method2():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed" 

baseUrl = "https://dev.playground.alexcook.dev/"
def test_getAllUsers():
	url = baseUrl + "api/users"
	payload = {}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	status_code = response.status_code
	assert status_code == 200

def test_createUser():
	# post create user
	url = baseUrl + "api/users"
	payload = {
		"firstName": "alex",
		"lastName": "cook",
		"age": 27,
		"address": "123 test"
	}
	headers = {
		"Content-Type": "application/json"
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	status_code = response.status_code
	assert status_code == 200
	
	# get specific user


# APIs:
# get last user
# get specific user
# create user
# update user
# delete user
# delete all

# Tests
# create user
# get specific user
# [x] get all users
# update user
# delete user
