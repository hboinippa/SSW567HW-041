import unittest

from GITHUBAPI import githubapi

class Testgithubapi(unittest.TestCase):
    def testgithub(self):
        self.assertEqual(githubapi('?'), False)
    def testgithub2(self):
        self.assertEqual(githubapi('hboinip'), False)
    def testgithub3(self):
        self.assertEqual(githubapi('SSW567HW-041'), False)
    def testgithub4(self):
        self.assertEqual(githubapi('demo'), True)



if __name__ == '__main__':
    print("Test cases are running")
    unittest.main()