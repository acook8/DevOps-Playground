import pytest
from seleniumbase import BaseCase

class UsersTestClass(BaseCase):
    
    def test_usersPage(self):
        # create test data
        # create user with api
        # verify user exists on ui
        # delete user with api
        url = "https://dev.playground.alexcook.dev"
        self.open(url)
        self.assert_text('DevOps Playground')
        self.click('#basic-navbar-nav > div > a:nth-child(2)')
        self.assert_text('Users')