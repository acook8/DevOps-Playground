import pytest
from seleniumbase import BaseCase

class UsersTestClass(BaseCase):
    
    def test_usersPage(self):
        url = "https://dev.playground.alexcook.dev"
        self.open(url)
        self.assert_text('DevOps Playground')
        self.click('#basic-navbar-nav > div > a:nth-child(2)')
        self.assert_text('Users')