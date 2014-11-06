import datetime
import unittest

from django.utils import timezone
from django.test import TestCase

class ImageSpaceTests(unittest.TestCase):
    def setUp(self):
        self.url="http://localhost:8000"
        self.email="John@doe.com"
        self.password="password"
    
    def tearDown(self):
        del self.url
    
    def test1(self):
        self.assertEqual(self.url,"http://localhost:8000")
    
    def test2(self):
        self.assertEqual(self.email,"John@doe.com")
        self.assertEqual(self.password,"password")
        "log in to the profile of John Doe"
    
    def test3(self):
        """
        url is not correct
        """
        self.assertNotEqual(self.url,"google.com")
    
    def test4(self):
        """
        Invalid Username/Password
        """
        self.assertNotEqual(self.email,"")
        self.assertNotEqual(self.password,"")


    


    
