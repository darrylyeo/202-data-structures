# Assignment:
# http://users.csc.calpoly.edu/~grader-ph/202/projects/p1/P1.pdf

import unittest
from lexicographic_permutations import *
from base_convert import *
from bears import *

class TestLexicographicPermutations(unittest.TestCase):
	def test0(self):
		self.assertEqual(perm_gen_lex(''), [])
		
	def test1(self):
		self.assertEqual(perm_gen_lex('a'), ['a'])
		
	def test2(self):
		self.assertEqual(perm_gen_lex('ab'), ['ab', 'ba'])
		
	def test3(self):
		self.assertEqual(perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
		
	def test4(self):
		self.assertEqual(perm_gen_lex('abcd'), [
			'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
			'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
			'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
			'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'
		])

class TestBaseConvert(unittest.TestCase):
	def test_base4(self):
		self.assertEqual(convert(30, 4), '132')
	
	def test_base2(self):
		self.assertEqual(convert(45, 2), '101101')
	
	def test_base16(self):
		self.assertEqual(convert(316, 16), '13C')


class TestBears(unittest.TestCase):
	def test_250(self):
		self.assertTrue(bears(250))
	
	def test_42(self):
		self.assertTrue(bears(42))
	
	def test_53(self):
		self.assertFalse(bears(53))
	
	def test_41(self):
		self.assertFalse(bears(41))

if __name__ == "__main__":
	unittest.main()
	