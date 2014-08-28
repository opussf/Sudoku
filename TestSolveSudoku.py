#!/usr/bin/env python
from solveSudoku import *
import unittest

board = sudokuboard.SudokuBoard(9)
board.loadFromFile("puzzles.txt")
#print board

class TestSolveSudoku(unittest.TestCase):
	simple = "8,6,,3,9,,4,5,7,5,9,7,4,8,,,6,3,3,4,,7,6,5,9,8,,,5,4,8,3,9,6,7,,7,,3,6,5,4,,9,8,9,8,6,,,7,3,4,5,4,3,9,,,,,,,6,,8,,,,,,,,7,5,,1,,,,"
	simpleSolved = "8,6,1,3,9,2,4,5,7,5,9,7,4,8,1,2,6,3,3,4,2,7,6,5,9,8,1,1,5,4,8,3,9,6,7,2,7,2,3,6,5,4,1,9,8,9,8,6,1,2,7,3,4,5,4,3,9,2,7,8,5,1,6,6,1,8,5,4,3,7,2,9,2,7,5,9,1,6,8,3,4"
	singleHidden = ",,,,,8,,2,,,,,2,6,,1,,3,,,,,,3,8,5,,2,,,,,,3,9,,,3,,,,,,,,4,,,,8,7,,,2,,2,,,5,,7,3,,,,4,,9,,,,,8,,,7,,6,,1,"
	singleValuePuzzle = ",,,,,8,,2,,,,,2,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
	def setUp(self):
		board = sudokuboard.SudokuBoard( 9 )
		board.initBoard( self.simple )
		self.Sudoku = SolveSudoku( board )
		self.sol = ['1','2','3','4','5','6','7','8','9']
		self.sqSol = [['1','2','3'],['4','5','6'],['7','8','9']]
	def test_solveLine_01(self):
		""" test solveLine_01 - 2 missing values """
		self.failIf(self.Sudoku.solveLine([None,'2','3','4',None,'6','7','8','9']), "Solution is indeterminate")
	def test_solveLine_02(self):
		""" test solveLine_02 value 1 missing """
		s = self.Sudoku.solveLine([None,'2','3','4','5','6','7','8','9'])
		self.assertEqual(s[0], self.sol, "Should have solved this")
	def test_solveLine_03(self):
		"""solveLine_03 value 5 missing """
		s = self.Sudoku.solveLine(['1','2','3','4',None,'6','7','8','9'])
		self.assertEqual(s[0], self.sol, "Should have solved this")
	def test_solveLine_04(self):
		"""0 Solvable rows"""
		Found = None
		for r in range(9):
			Found = Found or self.Sudoku.solveLine(self.Sudoku.board.getRow(r))
		self.failIf(Found, "No single solvable row should be found")
	def test_solveLine_05(self):
		"""0 Solvable cols"""
		Found = None
		for c in range(9):
			Found = Found or self.Sudoku.solveLine(self.Sudoku.board.getCol(c))
		self.failIf(Found, "No single solvable col should be found")
	def test_solveLine_06(self):
		"""0 Solvable squares"""
		Found = None
		Found = self.Sudoku.solveLine(self.Sudoku.board.getSquare(0,0,3)[1])
		self.failIf(Found, "This square is not solvable")
	def test_solveSquare_01( self ):
		""" solveSquare with 2 empty spots is not solvable """
		self.failIf(self.Sudoku.solveSquare([[None,'2','3'],['4',None,'6'],['7','8','9']]), "Solution is indeterminate")
	def test_solveSquare_02( self ):
		""" solveSquare is not really needed """
		s = self.Sudoku.solveSquare([[None,'2','3'],['4','5','6'],['7','8','9']])
		#self.assertEqual(s[0], self.sqSol, "Should have solved this")
	def test_buildUsed_01( self ):
		""" test buildUsed returns None list if value is set """
		self.assertEqual( self.Sudoku.buildUsed( 0, 0 ), [None]*self.Sudoku.board.size )
	def test_buildUsed_02( self ):
		""" test buildUsed returns expected values """
		self.assertEquals( self.Sudoku.buildUsed( 2, 0 ), [None,None,'3','4','5','6','7','8','9'], 
				"buildUsed should return a list of the values not usable for that box" )
	def test_buildUsed_03( self ):
		""" test buildUsed sets the notes on the board correctly """
		self.Sudoku.buildUsed( 2, 0 )
		self.assertEquals( self.Sudoku.board.getNotes( 2, 0 ), [None,None,'3','4','5','6','7','8','9'], 
				"buildUsed should set the list of the values not usable for that box for the board" )
	def test_buildUsed_04( self ):
		""" test_buildUsed_04 - single value, the value box """
		self.Sudoku.board.initBoard( self.singleValuePuzzle )
		self.assertEqual( self.Sudoku.buildUsed( 5, 0 ), [None]*self.Sudoku.board.size )
		self.failIf( self.Sudoku.board.getPossible( 5, 0 ) )
	def test_buildUsed_05( self ):
		""" test_buildUsed_04 - single value, the value row """
		self.Sudoku.board.initBoard( self.singleValuePuzzle )
		self.assertEqual( self.Sudoku.buildUsed( 0, 0 ), [None,'2',None,None,None,None,None,'8',None])
		poss = self.Sudoku.board.getPossible( 0, 0 )
		poss.sort()
		self.assertEqual( poss, ['1','3','4','5','6','7','9'] )
	def test_buildUsed_06( self ):
		""" test_buildUsed_04 - single value, the value col """
		self.Sudoku.board.initBoard( self.singleValuePuzzle )
		self.assertEqual( self.Sudoku.buildUsed( 5, 8 ), [None,None,None,None,None,None,None,'8',None])
		poss = self.Sudoku.board.getPossible( 5, 8 )
		poss.sort()
		self.assertEqual( poss, ['1','2','3','4','5','6','7','9'] )
	def test_buildUsed_07( self ):
		""" test_buildUsed_04 - single value, the value square """
		self.Sudoku.board.initBoard( self.singleValuePuzzle )
		self.assertEqual( self.Sudoku.buildUsed( 3, 2 ), [None,'2',None,None,None,None,None,'8',None])
		poss = self.Sudoku.board.getPossible( 3, 2 )
		poss.sort()
		self.assertEqual( poss, ['1','3','4','5','6','7','9'] )
	def test_buildUsedAll_01( self ):
		""" test that buildUsedAll sets the notes on the board correctly """
		self.Sudoku.buildUsedAll()
		self.assertEquals( self.Sudoku.board.getNotes( 6, 6 ), [None,None,'3','4',None,'6',None,None,'9'], 
				"buildUsedAll should set the list of the values not usable for all the boxes for the board" )
	def test_solveForSingleValues_01( self ):
		""" test that solveForSingleValues finds missing values and returns a list of 2 """
		self.Sudoku.buildUsedAll()
		moves = self.Sudoku.solveForSingleValues()
		self.assertEquals( len(moves), 2, "Two moves should have been found" )
	def test_solveForSingleValues_02( self ):
		""" test that solveForSingleValues finds missing values and returns a list of tuples or 3 values each """
		moves = self.Sudoku.solveForSingleValues()
		self.assertEquals( type( moves ), type( [] ), "moves should be a list" )
		for m in moves:
			self.assertEquals( type(m), type( () ), "values should be in a tuple" )
	def test_solveForSingleMissing_01( self ):
		self.Sudoku.buildUsedAll()
		moves = self.Sudoku.solveForSingleMissing()
		self.assertEquals( len( moves ), 31 )
		self.assertEquals( len( moves ), 31, "31 moves should have been found" )
	def test_solveForSingleMissing_02( self ):
		self.Sudoku.buildUsedAll()
		moves = self.Sudoku.solveForSingleMissing()
		self.assertEquals( type( moves ), type( [] ) )
		for m in moves:
			self.assertEquals( type(m), type( () ) )
	def test_solveBoard_01( self ):
		""" tests that solveBoard will solve the simple puzzle """
		self.Sudoku.solveBoard()
		self.failUnless( self.Sudoku.board.isSolved() )
	def test_solveForHiddenSingle_01( self ):
		""" test_solveForHiddenSingle_01 - row 1 should find a hidden 7 at 0,1 """
		board.initBoard( self.singleHidden )
		self.Sudoku = SolveSudoku( board )
		self.Sudoku.buildUsedAll()
		moves = 1
		while (moves > 0):
			moves = 0
			moves += len(self.Sudoku.solveForSingleValues())
			moves += len(self.Sudoku.solveForSingleMissing())
		self.assertEquals( self.Sudoku.solveForHiddenSingle(), [(0,1,'7','hs')] )
########  Locked Pairs  ##########
	def test_eliminateLockedPairValues_01( self ):
		self.Sudoku.buildUsedAll()
		self.Sudoku.eliminateLockedPairValues(1)
		self.assertEquals( self.Sudoku.board.getPossible(8,6), ['6'] )
########  Single pair ###########
#	def test_eliminateSinglePairs( self ):
#		moves = self.Sudoku.eliminateSinglePairs()
#	def test_eliminateSinglePairs2( self ):
#		moves = self.Sudoku.eliminateSinglePairs()
		

def suite():
	suite = unittest.TestSuite()
	suite.addTests( unittest.makeSuite( TestSolveSudoku ) )
	return suite
		
if __name__ == "__main__":
	unittest.main()
