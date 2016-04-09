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
	def test_puzzle_126_txt( self ):
		self.solve.board.loadFromFile("puzzle-126.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-126.txt fails:"
			self.printOutput()
			self.fail("puzzle-126.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_129_txt( self ):
		self.solve.board.loadFromFile("puzzle-129.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-129.txt fails:"
			self.printOutput()
			self.fail("puzzle-129.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_130_txt( self ):
		self.solve.board.loadFromFile("puzzle-130.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-130.txt fails:"
			self.printOutput()
			self.fail("puzzle-130.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_148_txt( self ):
		self.solve.board.loadFromFile("puzzle-148.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-148.txt fails:"
			self.printOutput()
			self.fail("puzzle-148.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
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
	def test_puzzle_167_txt( self ):
		self.solve.board.loadFromFile("puzzle-167.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-167.txt fails:"
			self.printOutput()
			self.fail("puzzle-167.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_168_txt( self ):
		self.solve.board.loadFromFile("puzzle-168.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-168.txt fails:"
			self.printOutput()
			self.fail("puzzle-168.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_169_txt( self ):
		self.solve.board.loadFromFile("puzzle-169.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-169.txt fails:"
			self.printOutput()
			self.fail("puzzle-169.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_170_txt( self ):
		self.solve.board.loadFromFile("puzzle-170.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-170.txt fails:"
			self.printOutput()
			self.fail("puzzle-170.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_171_txt( self ):
		self.solve.board.loadFromFile("puzzle-171.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-171.txt fails:"
			self.printOutput()
			self.fail("puzzle-171.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_172_txt( self ):
		self.solve.board.loadFromFile("puzzle-172.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-172.txt fails:"
			self.printOutput()
			self.fail("puzzle-172.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_173_txt( self ):
		self.solve.board.loadFromFile("puzzle-173.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-173.txt fails:"
			self.printOutput()
			self.fail("puzzle-173.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_174_txt( self ):
		self.solve.board.loadFromFile("puzzle-174.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-174.txt fails:"
			self.printOutput()
			self.fail("puzzle-174.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
	def test_puzzle_175_txt( self ):
		self.solve.board.loadFromFile("puzzle-175.txt")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "puzzle-175.txt fails:"
			self.printOutput()
			self.fail("puzzle-175.txt can only be solved to " + str(self.solve.board.solvedPerCent()) + "%")
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