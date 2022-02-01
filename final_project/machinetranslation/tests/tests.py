import unittest

from translator import englishtofrench, frenchtoenglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench(""),"") #Test when the world '' and ''.
        self.assertEqual(englishtofrench("Hello"), "Bonjour") #Test when the world 'Hello' and 'Bonjour'.
       

class Testfrenchtoenglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish(""),"") #Test when the world '' and ''.
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello") #Test when the world 'Bonjour' and 'Hello'.
     
unittest.main()