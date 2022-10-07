import unittest

from GITHUBAPI import githubapi

class Testgithubapi(unittest.TestCase):
    def testgithub(self):
        self.assertEqual(githubapi('?'), False)
    def testgithub2(self):
        self.assertEqual(githubapi('Monicaprojects21'), True)
    def testgithub3(self):
        self.assertEqual(githubapi('HW04'), False)
    def testgithub4(self):
        self.assertEqual(githubapi('demo'), False)
    def testgithub5(self):
            self.assertEqual(githubapi('00'), True)


if __name__ == '__main__':
    print("Test cases are running")
    unittest.main()