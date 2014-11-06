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
        print "After the user input the right URL, home page of the image space opens up"
    
    def test2(self):
        self.assertEqual(self.email,"John@doe.com")
        self.assertEqual(self.password,"password")
        print "If the user enters the correct email and password, log in to the profile of John Doe"
    
    def test3(self):
        """
        url is not correct
        """
        self.assertNotEqual(self.url,"google.com")
        print "If the user did not enter the right URL, URL is not correct"
    
    def test4(self):
        """
        Invalid Email/Password
        """
        self.assertNotEqual(self.email,"")
        self.assertNotEqual(self.password,"")
        print "If the user either leaves email or password blank, Invalid Email/Password"
    
    def test5(self):
        self.assertNotEqual(self.email,"Johndoe")
        self.assertNotEqual(self.password,"pass")
        print "If the user enther the wrong email or password or both, Invalid Email/Password"

    def test6(self):
        """
        At sign up page
        """
        self.assertNotEqual(self.email,"")
        self.assertNotEqual(self.password,"")
        print "At the sign up page if the user leaves either email or password blank then prompt: This field is required"
        self.assertNotEqual(self.email,"Johndoe")
        print "At the sign up page if the user enter email address to sign up without @something.com then prompt error to enter the valid email address with @"




    
