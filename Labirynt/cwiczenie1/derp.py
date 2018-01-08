'''
Created on 8 sty 2018

@author: student
'''
import unittest

def primes(liczba):
    for i in range(1,liczba):
        if liczba%i==0:
            return False
        else:
            True

class Test(unittest.TestCase):


    def test_czy_minus_4_jest_pierwsze(self):
        self.assertFalse(primes(-4),'-4 nie jest pierwsza!')

    def test_czy_7_jest_pierwsze(self):
        self.assertFalse(primes(7),'7 jest pierwsza!')
        
    def test_czy_24_jest_pierwsze(self):
        self.assertFalse(primes(24),'24 nie jest pierwsza!')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()