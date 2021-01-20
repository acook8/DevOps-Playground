import pytest
import requests
import json
import random
from faker import Faker
import userApi_helpers as helper
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
    response = helper.getUsers(url)
    status_code = response.status_code
    assert status_code == 200

def test_createUser():
    
    # Create test data
    fake = Faker()
    firstname = fake.first_name()
    lastname = fake.last_name()
    age = random.randint(10,80)
    address = fake.address()
    url = baseUrl + "api/users"
    
    # Create user
    response = helper.createUser(url, firstname, lastname, age, address)
    status_code = response.status_code
    assert status_code == 200
    result = response.json()
    userId = result.get('userId')
    
    # Validate data
    url = url + "/" + str(userId)
    response2 = helper.getUsers(url)
    status_code2 = response2.status_code
    assert status_code == 200
    result2 = response2.json()
    userIdResult = result2.get('userId')
    firstnameResult = result2.get('firstname')
    lastnameResult = result2.get('lastname')
    ageResult = result2.get('age')
    addressResult = result2.get('address')
    
    assert userId == userIdResult
    assert firstname == firstnameResult
    assert lastname == lastnameResult
    assert age == ageResult
    assert address == addressResult


    # Cleanup

    # Validate Cleanup

# APIs:
# get all users
# get specific user
# create user
# update user
# delete user
# delete all

# Tests
# [x] create user
# [x] get specific user
# [x] get all users
# update user
# delete user
