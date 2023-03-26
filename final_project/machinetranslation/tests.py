"""
    Module for unit test of language translator
"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):

    def test1(self):

        # test when 'Hello' is passed the result is 'bonjour'
        self.assertEqual(english_to_french('Hello').lower(), 'bonjour')
        # test when 'Hello' is passed the result is 'bonjour'
        self.assertNotEqual(english_to_french('Hello').lower(), 'hello')
        # test when null string is passed the ApiException is raised
        self.assertNotEqual(english_to_french(''),'')

class TestFrenchToEnglish(unittest.TestCase):

    def test1(self):
        # test when 'Bonjour' is passed the result is 'hello'
        self.assertEqual(french_to_english('Bonjour').lower(), 'hello')
        # test when 'Bonjour' is passed the result is 'hello'
        self.assertNotEqual(french_to_english('Bonjour').lower(), 'bonjour')
        # test when null string is passed the ApiException is raised
        self.assertNotEqual(french_to_english(''),'')

unittest.main()
