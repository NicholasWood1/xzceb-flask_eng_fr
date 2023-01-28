import unittest

from translator import english_to_french, french_to_english

class E2FTest(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour', 'It worked?')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir', 'It worked?')
        self.assertIsNone(english_to_french(None))

        

class F2ETest(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello', 'It worked?')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye', 'It worked?') 
        self.assertIsNone(french_to_english(None)) 
        
unittest.main()