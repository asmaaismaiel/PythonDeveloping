from Tasks.Lab1 import *
import unittest


class TestStringMethods(unittest.TestCase):
    #vowel
    def test_upper(self):
        self.assertEqual(vowel3("mobile"), 'mbl')
#multiply

    def test_list(self):
        self.assertEqual(num(4), [[1], [2, 4], [3, 6, 9], [4, 8, 12, 16]])
#area

    def test_the_area(self):
        self.assertEqual(area("r", 2), "4")
#create dic

    def test_the_sp(self):
        self.assertEqual(
            sp(["slaa", "ahmed", "mahdy"]), [('a', 'ahmed'), ('m', 'mahdy'),
                                             ('s', 'slaa')])


#index

    def test_the_Index(self):
        self.assertEqual(strIndex("iihihhiii", "i"), [0, 1, 3, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()