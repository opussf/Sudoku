#!/usr/bin/env python
import unittest
import solveSudoku
import sudokuboard

class TestSudokuFiles( unittest.TestCase ):
	def setUp( self ):
		self.board = sudokuboard.SudokuBoard(9)
		self.solve = solveSudoku.SolveSudoku( self.board )
	def printOutput( self ):
		self.solve.board.outType = "Base"
		freshBoard = str(self.solve.board).split("\n")
		self.solve.board.outType = "Full"	
		doneBoard = str(self.solve.board).split("\n")
		moves = [["%s %s %i,%i" % (m[2],m[3],m[0],m[1])] for m in self.solve.getAllMoves()]
		moveList = [[] for i in range(13)]
		line,mc = 0, 0
		for m in moves:
			if line >= 13:
				continue
			moveList[line].extend(m)
			mc += 1
			if mc >= 6:
				line, mc = line+1, 0
		for line in range(len(freshBoard)):
			print "%s	%s	%s" % ( freshBoard[line], doneBoard[line], " | ".join(moveList[line]) )
		print "="*80

	def test_puzzle_105_txt( self ):
		self.solve.board.loadFromFile("puzzle-105.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-105.txt fails:"
			self.printOutput()
			self.fail("puzzle-105.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_106_txt( self ):
		self.solve.board.loadFromFile("puzzle-106.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-106.txt fails:"
			self.printOutput()
			self.fail("puzzle-106.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_109_txt( self ):
		self.solve.board.loadFromFile("puzzle-109.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-109.txt fails:"
			self.printOutput()
			self.fail("puzzle-109.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_113_txt( self ):
		self.solve.board.loadFromFile("puzzle-113.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-113.txt fails:"
			self.printOutput()
			self.fail("puzzle-113.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_114_txt( self ):
		self.solve.board.loadFromFile("puzzle-114.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-114.txt fails:"
			self.printOutput()
			self.fail("puzzle-114.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_117_txt( self ):
		self.solve.board.loadFromFile("puzzle-117.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-117.txt fails:"
			self.printOutput()
			self.fail("puzzle-117.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266661680_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266661680.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266661680.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266661680.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266661708_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266661708.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266661708.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266661708.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266662607_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266662607.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266662607.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266662607.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266662609_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266662609.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266662609.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266662609.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663754_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663754.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663754.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663754.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663756_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663756.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663756.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663756.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663758_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663758.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663758.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663758.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663769_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663769.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663769.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663769.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663773_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663773.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663773.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663773.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663776_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663776.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663776.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663776.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663886_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663886.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663886.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663886.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663911_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663911.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663911.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663911.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663914_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663914.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663914.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663914.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266663918_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266663918.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266663918.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266663918.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664640_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664640.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664640.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664640.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664673_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664673.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664673.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664673.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664677_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664677.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664677.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664677.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664679_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664679.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664679.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664679.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664689_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664689.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664689.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664689.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664817_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664817.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664817.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664817.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664821_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664821.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664821.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664821.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664824_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664824.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664824.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664824.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664830_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664830.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664830.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664830.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266664858_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266664858.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266664858.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266664858.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665100_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665100.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665100.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665100.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665130_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665130.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665130.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665130.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665157_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665157.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665157.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665157.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665398_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665398.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665398.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665398.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665400_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665400.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665400.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665400.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665402_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665402.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665402.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665402.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665407_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665407.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665407.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665407.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665412_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665412.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665412.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665412.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665485_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665485.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665485.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665485.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665487_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665487.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665487.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665487.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665491_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665491.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665491.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665491.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665500_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665500.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665500.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665500.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665516_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665516.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665516.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665516.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665644_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665644.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665644.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665644.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665696_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665696.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665696.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665696.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665699_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665699.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665699.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665699.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665701_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665701.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665701.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665701.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665890_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665890.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665890.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665890.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665895_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665895.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665895.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665895.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665899_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665899.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665899.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665899.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665902_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665902.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665902.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665902.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665903_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665903.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665903.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665903.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665975_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665975.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665975.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665975.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266665981_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266665981.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266665981.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266665981.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666007_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666007.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666007.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666007.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666011_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666011.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666011.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666011.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666014_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666014.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666014.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666014.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666052_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666052.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666052.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666052.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666062_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666062.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666062.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666062.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666066_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666066.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666066.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666066.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666068_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666068.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666068.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666068.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666072_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666072.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666072.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666072.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266666074_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266666074.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266666074.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266666074.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703100_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703100.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703100.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703100.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703101_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703101.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703101.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703101.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703102_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703102.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703102.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703102.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703103_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703103.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703103.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703103.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703104_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703104.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703104.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703104.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703105_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703105.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703105.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703105.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703138_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703138.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703138.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703138.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703139_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703139.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703139.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703139.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703141_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703141.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703141.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703141.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703142_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703142.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703142.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703142.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703144_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703144.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703144.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703144.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703145_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703145.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703145.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703145.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703398_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703398.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703398.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703398.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703399_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703399.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703399.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703399.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703401_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703401.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703401.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703401.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703402_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703402.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703402.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703402.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703403_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703403.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703403.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703403.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266703404_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266703404.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266703404.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266703404.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706457_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706457.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706457.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706457.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706458_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706458.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706458.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706458.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706459_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706459.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706459.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706459.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706460_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706460.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706460.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706460.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706461_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706461.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706461.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706461.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706469_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706469.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706469.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706469.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706471_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706471.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706471.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706471.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706472_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706472.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706472.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706472.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706473_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706473.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706473.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706473.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706474_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706474.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706474.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706474.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706504_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706504.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706504.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706504.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706506_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706506.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706506.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706506.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706507_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706507.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706507.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706507.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706508_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706508.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706508.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706508.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706509_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706509.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706509.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706509.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706510_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706510.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706510.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706510.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706544_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706544.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706544.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706544.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706546_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706546.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706546.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706546.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706547_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706547.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706547.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706547.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706548_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706548.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706548.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706548.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706549_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706549.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706549.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706549.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706583_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706583.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706583.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706583.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706584_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706584.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706584.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706584.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706585_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706585.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706585.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706585.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706586_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706586.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706586.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706586.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706587_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706587.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706587.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706587.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706612_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706612.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706612.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706612.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706613_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706613.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706613.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706613.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706614_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706614.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706614.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706614.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706615_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706615.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706615.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706615.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706616_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706616.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706616.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706616.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266706617_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266706617.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266706617.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266706617.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266707899_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266707899.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266707899.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266707899.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266707900_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266707900.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266707900.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266707900.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266707901_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266707901.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266707901.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266707901.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266707902_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266707902.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266707902.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266707902.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266707903_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266707903.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266707903.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266707903.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266707904_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266707904.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266707904.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266707904.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266715667_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266715667.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266715667.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266715667.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266715668_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266715668.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266715668.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266715668.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266715670_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266715670.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266715670.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266715670.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266715671_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266715671.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266715671.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266715671.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266715672_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266715672.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266715672.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266715672.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266715673_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266715673.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266715673.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266715673.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266819543_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266819543.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266819543.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266819543.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266819544_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266819544.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266819544.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266819544.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266819546_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266819546.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266819546.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266819546.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266819547_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266819547.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266819547.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266819547.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266819548_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266819548.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266819548.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266819548.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266819550_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266819550.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266819550.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266819550.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266825862_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266825862.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266825862.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266825862.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266825863_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266825863.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266825863.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266825863.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266825865_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266825865.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266825865.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266825865.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266825866_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266825866.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266825866.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266825866.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266825867_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266825867.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266825867.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266825867.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1266825869_txt( self ):
		self.solve.board.loadFromFile("puzzle-1266825869.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1266825869.txt fails:"
			self.printOutput()
			self.fail("puzzle-1266825869.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267145487_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267145487.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267145487.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267145487.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267145488_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267145488.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267145488.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267145488.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267145489_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267145489.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267145489.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267145489.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267145491_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267145491.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267145491.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267145491.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267145493_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267145493.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267145493.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267145493.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267145494_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267145494.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267145494.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267145494.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267147893_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267147893.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267147893.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267147893.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267147897_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267147897.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267147897.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267147897.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267147901_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267147901.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267147901.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267147901.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267147904_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267147904.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267147904.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267147904.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267147905_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267147905.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267147905.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267147905.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267147908_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267147908.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267147908.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267147908.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267148570_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267148570.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267148570.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267148570.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267148573_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267148573.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267148573.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267148573.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267148578_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267148578.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267148578.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267148578.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267148582_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267148582.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267148582.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267148582.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267148586_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267148586.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267148586.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267148586.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267148589_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267148589.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267148589.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267148589.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267153367_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267153367.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267153367.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267153367.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267153368_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267153368.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267153368.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267153368.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267153370_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267153370.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267153370.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267153370.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267153371_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267153371.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267153371.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267153371.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267153372_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267153372.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267153372.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267153372.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_1267153373_txt( self ):
		self.solve.board.loadFromFile("puzzle-1267153373.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-1267153373.txt fails:"
			self.printOutput()
			self.fail("puzzle-1267153373.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_149_txt( self ):
		self.solve.board.loadFromFile("puzzle-149.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-149.txt fails:"
			self.printOutput()
			self.fail("puzzle-149.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_150_txt( self ):
		self.solve.board.loadFromFile("puzzle-150.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-150.txt fails:"
			self.printOutput()
			self.fail("puzzle-150.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_152_txt( self ):
		self.solve.board.loadFromFile("puzzle-152.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-152.txt fails:"
			self.printOutput()
			self.fail("puzzle-152.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_154_txt( self ):
		self.solve.board.loadFromFile("puzzle-154.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-154.txt fails:"
			self.printOutput()
			self.fail("puzzle-154.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_156_txt( self ):
		self.solve.board.loadFromFile("puzzle-156.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-156.txt fails:"
			self.printOutput()
			self.fail("puzzle-156.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_157_txt( self ):
		self.solve.board.loadFromFile("puzzle-157.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-157.txt fails:"
			self.printOutput()
			self.fail("puzzle-157.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_158_txt( self ):
		self.solve.board.loadFromFile("puzzle-158.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-158.txt fails:"
			self.printOutput()
			self.fail("puzzle-158.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_159_txt( self ):
		self.solve.board.loadFromFile("puzzle-159.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-159.txt fails:"
			self.printOutput()
			self.fail("puzzle-159.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_160_txt( self ):
		self.solve.board.loadFromFile("puzzle-160.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-160.txt fails:"
			self.printOutput()
			self.fail("puzzle-160.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_161_txt( self ):
		self.solve.board.loadFromFile("puzzle-161.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-161.txt fails:"
			self.printOutput()
			self.fail("puzzle-161.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_162_txt( self ):
		self.solve.board.loadFromFile("puzzle-162.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-162.txt fails:"
			self.printOutput()
			self.fail("puzzle-162.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_164_txt( self ):
		self.solve.board.loadFromFile("puzzle-164.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-164.txt fails:"
			self.printOutput()
			self.fail("puzzle-164.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_165_txt( self ):
		self.solve.board.loadFromFile("puzzle-165.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-165.txt fails:"
			self.printOutput()
			self.fail("puzzle-165.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_166_txt( self ):
		self.solve.board.loadFromFile("puzzle-166.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-166.txt fails:"
			self.printOutput()
			self.fail("puzzle-166.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_176_txt( self ):
		self.solve.board.loadFromFile("puzzle-176.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-176.txt fails:"
			self.printOutput()
			self.fail("puzzle-176.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_177_txt( self ):
		self.solve.board.loadFromFile("puzzle-177.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-177.txt fails:"
			self.printOutput()
			self.fail("puzzle-177.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_178_txt( self ):
		self.solve.board.loadFromFile("puzzle-178.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-178.txt fails:"
			self.printOutput()
			self.fail("puzzle-178.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_179_txt( self ):
		self.solve.board.loadFromFile("puzzle-179.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-179.txt fails:"
			self.printOutput()
			self.fail("puzzle-179.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_180_txt( self ):
		self.solve.board.loadFromFile("puzzle-180.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-180.txt fails:"
			self.printOutput()
			self.fail("puzzle-180.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_181_txt( self ):
		self.solve.board.loadFromFile("puzzle-181.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-181.txt fails:"
			self.printOutput()
			self.fail("puzzle-181.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_182_txt( self ):
		self.solve.board.loadFromFile("puzzle-182.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-182.txt fails:"
			self.printOutput()
			self.fail("puzzle-182.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_183_txt( self ):
		self.solve.board.loadFromFile("puzzle-183.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-183.txt fails:"
			self.printOutput()
			self.fail("puzzle-183.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_184_txt( self ):
		self.solve.board.loadFromFile("puzzle-184.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-184.txt fails:"
			self.printOutput()
			self.fail("puzzle-184.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_185_txt( self ):
		self.solve.board.loadFromFile("puzzle-185.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-185.txt fails:"
			self.printOutput()
			self.fail("puzzle-185.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_186_txt( self ):
		self.solve.board.loadFromFile("puzzle-186.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-186.txt fails:"
			self.printOutput()
			self.fail("puzzle-186.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_187_txt( self ):
		self.solve.board.loadFromFile("puzzle-187.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-187.txt fails:"
			self.printOutput()
			self.fail("puzzle-187.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_188_txt( self ):
		self.solve.board.loadFromFile("puzzle-188.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-188.txt fails:"
			self.printOutput()
			self.fail("puzzle-188.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_189_txt( self ):
		self.solve.board.loadFromFile("puzzle-189.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-189.txt fails:"
			self.printOutput()
			self.fail("puzzle-189.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_190_txt( self ):
		self.solve.board.loadFromFile("puzzle-190.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-190.txt fails:"
			self.printOutput()
			self.fail("puzzle-190.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_191_txt( self ):
		self.solve.board.loadFromFile("puzzle-191.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-191.txt fails:"
			self.printOutput()
			self.fail("puzzle-191.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_192_txt( self ):
		self.solve.board.loadFromFile("puzzle-192.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-192.txt fails:"
			self.printOutput()
			self.fail("puzzle-192.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_193_txt( self ):
		self.solve.board.loadFromFile("puzzle-193.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-193.txt fails:"
			self.printOutput()
			self.fail("puzzle-193.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_194_txt( self ):
		self.solve.board.loadFromFile("puzzle-194.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-194.txt fails:"
			self.printOutput()
			self.fail("puzzle-194.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_195_txt( self ):
		self.solve.board.loadFromFile("puzzle-195.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-195.txt fails:"
			self.printOutput()
			self.fail("puzzle-195.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_196_txt( self ):
		self.solve.board.loadFromFile("puzzle-196.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-196.txt fails:"
			self.printOutput()
			self.fail("puzzle-196.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_197_txt( self ):
		self.solve.board.loadFromFile("puzzle-197.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-197.txt fails:"
			self.printOutput()
			self.fail("puzzle-197.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_198_txt( self ):
		self.solve.board.loadFromFile("puzzle-198.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-198.txt fails:"
			self.printOutput()
			self.fail("puzzle-198.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_199_txt( self ):
		self.solve.board.loadFromFile("puzzle-199.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-199.txt fails:"
			self.printOutput()
			self.fail("puzzle-199.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_200_txt( self ):
		self.solve.board.loadFromFile("puzzle-200.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-200.txt fails:"
			self.printOutput()
			self.fail("puzzle-200.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_201_txt( self ):
		self.solve.board.loadFromFile("puzzle-201.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-201.txt fails:"
			self.printOutput()
			self.fail("puzzle-201.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_202_txt( self ):
		self.solve.board.loadFromFile("puzzle-202.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-202.txt fails:"
			self.printOutput()
			self.fail("puzzle-202.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_203_txt( self ):
		self.solve.board.loadFromFile("puzzle-203.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-203.txt fails:"
			self.printOutput()
			self.fail("puzzle-203.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_204_txt( self ):
		self.solve.board.loadFromFile("puzzle-204.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-204.txt fails:"
			self.printOutput()
			self.fail("puzzle-204.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_205_txt( self ):
		self.solve.board.loadFromFile("puzzle-205.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-205.txt fails:"
			self.printOutput()
			self.fail("puzzle-205.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_D7528_B_txt( self ):
		self.solve.board.loadFromFile("puzzle-D7528-B.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-D7528-B.txt fails:"
			self.printOutput()
			self.fail("puzzle-D7528-B.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_D7578_B_txt( self ):
		self.solve.board.loadFromFile("puzzle-D7578-B.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-D7578-B.txt fails:"
			self.printOutput()
			self.fail("puzzle-D7578-B.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_D7608_A_txt( self ):
		self.solve.board.loadFromFile("puzzle-D7608-A.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-D7608-A.txt fails:"
			self.printOutput()
			self.fail("puzzle-D7608-A.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_D7608_B_txt( self ):
		self.solve.board.loadFromFile("puzzle-D7608-B.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-D7608-B.txt fails:"
			self.printOutput()
			self.fail("puzzle-D7608-B.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_D7628_A_txt( self ):
		self.solve.board.loadFromFile("puzzle-D7628-A.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-D7628-A.txt fails:"
			self.printOutput()
			self.fail("puzzle-D7628-A.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_D7628_B_txt( self ):
		self.solve.board.loadFromFile("puzzle-D7628-B.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-D7628-B.txt fails:"
			self.printOutput()
			self.fail("puzzle-D7628-B.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_D7708_B_txt( self ):
		self.solve.board.loadFromFile("puzzle-D7708-B.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-D7708-B.txt fails:"
			self.printOutput()
			self.fail("puzzle-D7708-B.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_ebook_page10_txt( self ):
		self.solve.board.loadFromFile("puzzle-ebook-page10.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-ebook-page10.txt fails:"
			self.printOutput()
			self.fail("puzzle-ebook-page10.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hard001_txt( self ):
		self.solve.board.loadFromFile("puzzle-hard001.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hard001.txt fails:"
			self.printOutput()
			self.fail("puzzle-hard001.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hard002_txt( self ):
		self.solve.board.loadFromFile("puzzle-hard002.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hard002.txt fails:"
			self.printOutput()
			self.fail("puzzle-hard002.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hard003_txt( self ):
		self.solve.board.loadFromFile("puzzle-hard003.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hard003.txt fails:"
			self.printOutput()
			self.fail("puzzle-hard003.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hard004_txt( self ):
		self.solve.board.loadFromFile("puzzle-hard004.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hard004.txt fails:"
			self.printOutput()
			self.fail("puzzle-hard004.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hard005_txt( self ):
		self.solve.board.loadFromFile("puzzle-hard005.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hard005.txt fails:"
			self.printOutput()
			self.fail("puzzle-hard005.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hard006_txt( self ):
		self.solve.board.loadFromFile("puzzle-hard006.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hard006.txt fails:"
			self.printOutput()
			self.fail("puzzle-hard006.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hard007_txt( self ):
		self.solve.board.loadFromFile("puzzle-hard007.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hard007.txt fails:"
			self.printOutput()
			self.fail("puzzle-hard007.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hard120_txt( self ):
		self.solve.board.loadFromFile("puzzle-hard120.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hard120.txt fails:"
			self.printOutput()
			self.fail("puzzle-hard120.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_hint_txt( self ):
		self.solve.board.loadFromFile("puzzle-hint.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-hint.txt fails:"
			self.printOutput()
			self.fail("puzzle-hint.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_norm135_txt( self ):
		self.solve.board.loadFromFile("puzzle-norm135.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-norm135.txt fails:"
			self.printOutput()
			self.fail("puzzle-norm135.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_norm136_txt( self ):
		self.solve.board.loadFromFile("puzzle-norm136.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-norm136.txt fails:"
			self.printOutput()
			self.fail("puzzle-norm136.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_norm137_txt( self ):
		self.solve.board.loadFromFile("puzzle-norm137.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-norm137.txt fails:"
			self.printOutput()
			self.fail("puzzle-norm137.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_norm138_txt( self ):
		self.solve.board.loadFromFile("puzzle-norm138.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-norm138.txt fails:"
			self.printOutput()
			self.fail("puzzle-norm138.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_sfgate_02182010_txt( self ):
		self.solve.board.loadFromFile("puzzle-sfgate-02182010.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-sfgate-02182010.txt fails:"
			self.printOutput()
			self.fail("puzzle-sfgate-02182010.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_sfgate_02192010_txt( self ):
		self.solve.board.loadFromFile("puzzle-sfgate-02192010.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-sfgate-02192010.txt fails:"
			self.printOutput()
			self.fail("puzzle-sfgate-02192010.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_sfgate_02202010_txt( self ):
		self.solve.board.loadFromFile("puzzle-sfgate-02202010.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-sfgate-02202010.txt fails:"
			self.printOutput()
			self.fail("puzzle-sfgate-02202010.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_tip20_txt( self ):
		self.solve.board.loadFromFile("puzzle-tip20.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-tip20.txt fails:"
			self.printOutput()
			self.fail("puzzle-tip20.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_ups112_txt( self ):
		self.solve.board.loadFromFile("puzzle-ups112.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-ups112.txt fails:"
			self.printOutput()
			self.fail("puzzle-ups112.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_ups114_txt( self ):
		self.solve.board.loadFromFile("puzzle-ups114.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-ups114.txt fails:"
			self.printOutput()
			self.fail("puzzle-ups114.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_ups116_txt( self ):
		self.solve.board.loadFromFile("puzzle-ups116.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-ups116.txt fails:"
			self.printOutput()
			self.fail("puzzle-ups116.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_ups119_txt( self ):
		self.solve.board.loadFromFile("puzzle-ups119.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-ups119.txt fails:"
			self.printOutput()
			self.fail("puzzle-ups119.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzles_txt( self ):
		self.solve.board.loadFromFile("puzzles.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzles.txt fails:"
			self.printOutput()
			self.fail("puzzles.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")

def suite():
	suite = unittest.TestSuite()
	suite.addTests( unittest.makeSuite( TestSolveSudoku ) )
	return suite
		
if __name__ == "__main__":
	unittest.main()