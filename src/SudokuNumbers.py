#!/usr/bin/python
# SudokuNumbers.py
#########################################
# Some Sudoku boards have regions of numbers that sum to a given value.
# This is to create a list of possible values for the region
# 

import os

class SudokuNumbers(object):
	pass
	
	def setSum(self, sumIn):
		pass


if __name__ == "__main__":
	import unittest

	class TestSudokuBoard(unittest.TestCase):

		def setUp(self):
			self.SN = SudokuNumbers()

		def test_created(self):
			self.failUnless(self.SN, "Object should be created.")

		def test_setSum_setsSum(self):
			print self.SN.setSum(3)
			
			self.failUnless(self.SN.setSum, "Method should exist")
			

	unittest.main()
