import unittest
from src.main import carica_studenti

class TestMain(unittest.TestCase):
    def test_carica_studenti(self):
        studenti = carica_studenti('data/studenti.csv')
        self.assertEqual(len(studenti), 3)
        self.assertEqual(studenti[0]['nome'], 'Marco')

if __name__ == '__main__':
    unittest.main()
