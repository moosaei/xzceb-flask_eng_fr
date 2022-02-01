import unittest

from translator import englishtofrench, frenchtoenglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(englishtofrench("Hello"),"Hello") #Test when the world 'Hello' not  'Hello'.
        self.assertEqual(englishtofrench("Hello"), "Bonjour") #Test when the world 'Hello' and 'Bonjour'.
       

class Testfrenchtoenglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(frenchtoenglish("Bonjour"),"Bonjour") #Test when the world 'Bonjour' not 'Bonjour'.
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello") #Test when the world 'Bonjour' and 'Hello'.
     
unittest.main()