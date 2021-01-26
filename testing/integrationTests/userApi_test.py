import pytest
import requests
import json
import random
from faker import Faker
import userApi_helpers as helper
 

baseUrl = "https://dev.playground.alexcook.dev/"

def test_getAllUsers():
    url = baseUrl + "api/users"
    response = helper.getUsers(url)
    status_code = response.status_code
    assert status_code == 200

def test_createAndDeleteUser():
    
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
    assert status_code2 == 200
    result2 = response2.json()
    userIdResult = result2.get('userId')
    firstnameResult = result2.get('firstName')
    lastnameResult = result2.get('lastName')
    ageResult = result2.get('age')
    addressResult = result2.get('address')
    
    assert userId == userIdResult
    assert firstname == firstnameResult
    assert lastname == lastnameResult
    assert age == ageResult
    assert address == addressResult


    # Delete User
    responseDelete = helper.deleteUser(url)
    deleteStatusCode = responseDelete.status_code
    assert deleteStatusCode == 200

    # Validate Delete
    responseValidate = helper.getUsers(url)
    validateStatusCode = responseValidate.status_code
    assert validateStatusCode == 404

# def test_updateUser():
#     create user
#     update user
#     validate
#     delete user
