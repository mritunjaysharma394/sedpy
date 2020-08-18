import unittest
from sedpy import sedpy


class NamesTestCase(unittest.TestCase):
    def test_sedpy(self):
        sedpy.replace("4", "6", "test1.txt")
        f = open("test1.txt", "r")
        self.assertEqual(f.read(), "7 + 6 = 13")
        f.close()


if __name__ == '__main__':
    unittest.main()