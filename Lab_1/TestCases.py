from CalculateArea import *
from TheDictionary import *
from CharacterLocator import *
from MultiplicationTable import *
from VowelsRemoval import *
import unittest


class TestStringMethods(unittest.TestCase):
    # vowels
    def removeVowels(self):
        self.assertEqual(word("mobile"), 'mbl')
# multiply

    def calc(self):
        self.assertEqual(num(4), [[1], [2, 4], [3, 6, 9], [4, 8, 12, 16]])
        self.assertEqual(
            (num(5), [[1], [2, 4], [3, 6, 9], [4, 8, 12, 16], [5, 10, 15, 20, 25]]))
# area

    def calcArea(self):
        self.assertEqual(area("r", 2), "4.0")
        self.assertEqual(area("t", 2, 3), "3.0")
        self.assertEqual(area("c", 2), "12.56")
        self.assertEqual(area("r", 2, 5), "10.0")
# create dic

    def convert(self):
        self.assertEqual(convert(["ahmed", "fatma", "Ibrahim", "Islam", "Samah"]),
                         "{'S': ['Samah'], 'f': ['fatma'], 'a': ['ahmed'], 'I': ['Ibrahim', 'Islam']}")


# index

    def locate(self):
        self.assertEqual(locate("Islam", "m"), [4])
        self.assertEqual(locate("Aya", "a"), [2])


if __name__ == '__main__':
    unittest.main()
