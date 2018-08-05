class Myclass:

    def sum(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y


import unittest


class mytest(unittest.TestCase):
    # init
    def setUp(self):
        pass

    # quit
    def tearDown(self):
        pass

    # testCase
    def testSum(self):
        instance = Myclass()
        testResult = instance.sum(3, 4)
        self.assertEqual(testResult, 9, '3+4=7, not 9, so test fail')

    def testSub(self):
        instance = Myclass()
        testResult = instance.sub(8, 5)
        self.assertEqual(testResult, 3, 'test pass')

if __name__=="testSub":
    unittest.main()
