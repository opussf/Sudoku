#!/usr/bin/env python
import unittest
from sudokuboard import *

class TestSudokuBoard(unittest.TestCase):
	def setUp(self):
		""" setUP - create a 9x9 board, and load from puzzles.txt """
		self.myBoard = SudokuBoard(9)
		self.myBoard.initBoard( "5,,,,6,,7,,,,,,,7,8,,1,3,7,,9,5,,,6,8,,,9,,,,3,1,,5,3,,,8,,6,,,4,4,,5,7,,,,6,,,5,2,,,7,4,,6,8,6,,4,9,,,,,,,4,,2,,8,,7" )
		#self.myBoard.loadFromFile("sudokuboard.puzzle.test")
	def test_initBoard_01( self ):
		""" initBoard with a blank string """
		self.myBoard.initBoard( "" )
	def test_clearBoard_01( self ):
		""" does clearBoard clear baseBoard """
		self.assertEquals( self.myBoard.getValue( 0, 0 ), "5" )    # default set value
	def test_loadFromFile_01( self ):
		""" load a board from a file """
		fname = "sudokuboard.puzzle.test"
		puzzle = "6,,,,8,,4,,,,,,,5,,2,,9,,3,4,,,,,,,5,9,,,,,,,,,7,,,,,3,1,,,,,,,1,,,8,,2,3,,4,5,,,,,,,9,,,,,2,,,5,3,,8,,,1"
		self.myBoard.resetBoard()
		file( fname, "w" ).write(puzzle)
		line = self.myBoard.loadFromFile( fname )
		self.assertEquals( self.myBoard.getValue( 4, 0 ), "8" )
		self.assertEquals( self.myBoard.getValue( 1, 5 ), None )
		self.assertEquals( line, puzzle )
	def test_Print(self):
		""" fails if not string """
		self.assertEquals( type( self.myBoard.__str__() ), type( "" ), "Should return a string" )
	def test_getRow_01(self):
		""" tests to make sure getRow() only allows getting valid index """
		row = self.myBoard.getRow(10)
		self.failIf(row, "Returned invalid data")
	def test_getRow_02(self):
		""" tests to make sure getRow() only allows getting valid index """
		self.failIf(self.myBoard.getRow(9), "Returned invalid data")
	def test_getRow_03(self):
		""" tests to make sure getRow() only allows getting valid index """
		self.failIf(self.myBoard.getRow(-1), "Returned invalid data")
	def test_getRow_04(self):
		""" getRow() returns the correct list """
		row = self.myBoard.getRow(0)
		row0 = ['5',None,None,None,'6',None,'7',None,None]
		self.assertEquals(row, row0, "Bad Row returned")
	def test_getRow_05(self):
		""" getRow() returns the correct list """
		row = self.myBoard.getRow(1)
		row1 = [None,None,None,None,'7','8',None,'1','3']
		self.assertEquals(row, row1, "Bad Row returned")
	def test_getCol_01(self):
		""" getCol() fails on index out of range """
		self.failIf(self.myBoard.getCol(10), "Returned invalid data")
	def test_getCol_02(self):
		""" getCol() returns the correct list """
		col = self.myBoard.getCol(0)
		col0 = ['5',None,'7',None,'3','4',None,'8',None]
		self.assertEquals(col, col0, "Bad Col returned")
	def test_getCol_03(self):
		""" getCol() returns the correct list """
		col = self.myBoard.getCol(1)
		col1 = [None,None,None,'9',None,None,'5','6',None]
		self.assertEquals(col, col1, "Bad Col returned")
	def test_getSquare_01(self):
		""" getSquare() """
		self.failIf(self.myBoard.getSquare(-1,-1,9),"Invalid Range")
	def test_getSquare_02(self):
		self.failIf(self.myBoard.getSquare(9,9,1), "Invalid Range")
	def test_getSquare_03(self):
		self.failIf(self.myBoard.getSquare(8,9,1),"Invalid Range")
	def test_getSquare_04(self):
		self.failIf(self.myBoard.getSquare(0,0,0),"Invalid Range")
	def test_getSquare_05(self):
		self.failIf(self.myBoard.getSquare(8,8,2),"Invalid Range")
	def test_getSquare_06(self):
		""" getSquare() returns the correct lists """
		sq = self.myBoard.getSquare(0,0,1)
		sq001 = ([['5']], ['5'])
		self.assertEqual(sq, sq001, "Square of 1")
	def test_getSquare_07(self):
		""" getSquare() returns the correct lists """
		sq = self.myBoard.getSquare(8,8,1)
		sq881 = ([['7']], ['7'])
		self.assertEqual(sq, sq881, "Square of 1")
	def test_getSquare_08(self):
		""" getSquare() returns the correct info """
		sq = self.myBoard.getSquare(0,0,3)[0]
		sq003 = [['5',None,None],[None,None,None],['7',None,'9']]
		self.assertEqual(sq, sq003, "Bad Square")
	def test_getSquare_09(self):
		""" getSquare() returns the correct info """
		sq = self.myBoard.getSquare(0,0,3)[1]
		sq003 = ['5',None,None,None,None,None,'7',None,'9']
		self.assertEqual(sq, sq003, "Bad List from Square")
	def test_getSquare_10(self):
		""" getSquare() returns the correct 3x3 square """
		sq = self.myBoard.getSquare(3,0,3)[0]
		sq303 = [[None,'6',None],[None,'7','8'],['5',None,None]]
		self.assertEqual(sq, sq303, "Bad Square")
	def test_getSquare_11(self):
		""" getSquare() returns the correct 3x3 square """
		sq = self.myBoard.getSquare(6,0,3)[0]
		sq603 = [['7',None,None],[None,'1','3'],['6','8',None]]
		self.assertEqual(sq, sq603, "Bad Square")
	def test_getSquare_12(self):
		"""Get an 'odd' sized square"""
		sq = self.myBoard.getSquare(0,0,4)[0]
		sq004 = [['5', None, None, None], [None, None, None, None], ['7', None, '9', '5'], [None, '9', None, None]]
		self.assertEqual(sq, sq004, "Bad Square")
	def test_getSquare_13(self):
		"""Get the whole square"""
		sq = self.myBoard.getSquare(0,0,9)[0]
		sq009 = [['5', None, None, None, '6', None, '7', None, None], [None, None, None, None, '7', '8', None, '1', '3'], ['7', None, '9', '5', None, None, '6', '8', None], [None, '9', None, None, None, '3', '1', None, '5'], ['3', None, None, '8', None, '6', None, None, '4'], ['4', None, '5', '7', None, None, None, '6', None], [None, '5', '2', None, None, '7', '4', None, '6'], ['8', '6', None, '4', '9',None, None, None, None], [None, None, '4', None, '2', None, '8', None, '7']]
		self.assertEqual(sq, sq009, "Could not get whole square")
	def test_setValue_01( self ):
		self.failIf(self.myBoard.setValue(-1,-1,1), "Tried to set an invalid range")
	def test_setValue_02( self ):
		self.failIf(self.myBoard.setValue(8,9,1), "Tried to set an invalid range")
	def test_setValue_03( self ):
		self.failIf(self.myBoard.setValue(9,9,1), "Tried to set an invalid range")
	def test_setValue_04( self ):
		self.failIf(self.myBoard.setValue(1,1,10), "Tried to set an invalid value")
	def test_setValue_05( self ):
		""" setValue should fail whn trying to set a given value """
		self.failIf(self.myBoard.setValue(0,0,3), "Tried to set a given value")
	def test_setValue_06( self ):
		self.assertEqual(self.myBoard.setValue(8,7,1), 1, "Failed to properly set the value")
	def test_setValue_07( self ):
		"""Test setting a value for a non-base board"""
		self.failUnless(self.myBoard.setValue(8,7,1), "Should set")
		self.assertEqual(self.myBoard.setValue(8,7,3), 3, "Failed setting value")
	def test_setValue_08( self ):
		""" setValue() value is properly returned """
		self.myBoard.setValue(8,7,1)
		self.assertEqual(self.myBoard.getSquare(8,7,1), ([['1']], ['1']), "Should return the value set")
	def test_isSolved_01( self ):
		""" isSolved() should return true if solved """
		self.assertFalse(self.myBoard.isSolved(), "Should be false")
	def test_solvedPerCent_01( self ):
		""" solvedPerCent returns an integer value of percent solved """
		self.assertEqual( self.myBoard.solvedPerCent(), 45, "Should be about 45%" )
	def test_resetBoard_01( self ):
		""" resetBoard() should reset the board to base """
		self.myBoard.setValue(8,7,1)
		self.myBoard.resetBoard()
		self.assertEqual( self.myBoard.getSquare( 8, 7, 1), ([[None]], [None]), "Should return None value")
	def test_resetBoard_02( self ):
		""" resetBoard() should reset the board to base """
		self.myBoard.setValue(8,7,1)
		self.myBoard.setValue(7,0,4)
		self.myBoard.resetBoard()
		self.assertEqual( self.myBoard.getSquare( 7, 0, 1), ([[None]], [None]), "Should return None value")
	def test_getNotes_01( self ):
		""" getNotes() should error on out of range """
		self.failIf( self.myBoard.getNotes( 9, 9 ), "Should fail" )
	def test_getNotes_02( self ):
		self.failUnless( self.myBoard.getNotes( 0, 0 ), "Should pass" )
	def test_getNotes_03( self ):
		""" getNotes() should return a list of values for the x,y coord """
		self.assertEqual( self.myBoard.getNotes( 8, 7), [None]*9, "Should return a list of Nones")
	def test_setNoteValue_01( self ):
		""" setNoteValue() should fail on invalid coord """
		self.failIf(self.myBoard.setNoteValue(9,9,1), "Tried to setNoteValue for bad coord")
	def test_setNoteValue_02( self ):
		""" setNoteValue() should fail on out of range value """
		self.failIf(self.myBoard.setNoteValue(8,7,0), "Tried to set a bad value")
	def test_setNoteValue_03( self ):
		""" setNoteValue() should set a valid value """
		self.assertEqual( self.myBoard.setNoteValue( 8, 7, 1), 1, "Failed setting value")
	def test_setNoteValue_04( self ):
		""" setNoteValue() should set a note value as expected """
		self.myBoard.setNoteValue( 8, 7, 1 )
		self.assertEqual( self.myBoard.getNotes( 8, 7 ), ['1', None, None, None, None, None, None, None, None], "1 should be set" )
	def test_setNoteValue_05( self ):
		""" setNoteValue() should allow many settings """
		self.myBoard.setNoteValue( 8, 7, 1 )
		self.myBoard.setNoteValue( 8, 7, 2 )
		self.myBoard.setNoteValue( 8, 7, 3 )
		self.myBoard.setNoteValue( 8, 7, 4 )
		self.myBoard.setNoteValue( 8, 7, 5 )
		self.myBoard.setNoteValue( 8, 7, 6 )
		self.myBoard.setNoteValue( 8, 7, 7 )
		self.myBoard.setNoteValue( 8, 7, 8 )
		self.myBoard.setNoteValue( 8, 7, 9 )
		self.assertEqual( self.myBoard.getNotes( 8, 7 ), ['1','2','3','4','5','6','7','8','9'], "Should return a full notes list" )
	def test_setNoteValue_06( self ):
		""" setNoteValue() should set a value """
		self.myBoard.setNoteValue( 1, 0, 9 )
		self.myBoard.setNoteValue( 0, 1, 5 )
		self.assertEqual( self.myBoard.getNotes( 1, 0 ), [None,None,None,None,None,None,None,None,'9'], "Should have one value set" )
		self.assertEqual( self.myBoard.getNotes( 0, 1 ), [None,None,None,None,'5',None,None,None,None], "Should have one value set" )
	def test_clearNoteAt_01( self ):
		""" clearNoteAt() should not fail horribly on invalid exception """
		self.failIf( self.myBoard.clearNoteAt( 9, 9 ), "Should not throw exception" )
	def test_clearNoteAt_02( self ):
		""" clearNoteAt() for a valid coord """
		self.myBoard.setNoteValue( 8, 7, 5 )
		self.myBoard.clearNoteAt( 8, 7 )
		self.assertEqual( self.myBoard.getNotes( 8, 7 ), [None]*9, "Should return a list on Nones" )
	def test_clearNoteAt_03( self ):
		""" clearNoteAt() for no notes """
		self.myBoard.clearNoteAt( 8, 7 )
		self.assertEqual( self.myBoard.getNotes( 8, 7 ), [None]*9, "Should return a list on Nones" )
	def test_getPossible_01( self ):
		""" test_getPossible_01 - returns full set"""
		possible = self.myBoard.getPossible( 8, 7 )
		possible.sort()
		self.assertEqual( possible, ['1','2','3','4','5','6','7','8','9'], "Should return a full list")
	def test_getPossible_02( self ):
		""" test_getPossible_02 - returns a partial set """
		self.myBoard.setNoteValue( 8, 7, 5 )
		possible = self.myBoard.getPossible( 8, 7 )
		possible.sort()
		self.assertEqual( possible, ['1','2','3','4','6','7','8','9'], "Should return a list with no 5")
	def test_getPossible_03( self ):
		""" test_getPossible_03 - returns None if value is set """
		self.myBoard.setValue( 8, 7, 5 )
		possible = self.myBoard.getPossible( 8, 7 )
		self.assertEqual( possible, None )
	def test_hasVals_01( self ):
		""" test_hasVals_01 - tests that the board has a set of values """
		self.assertEqual( self.myBoard.vals, ['1','2','3','4','5','6','7','8','9'] )

def suite():
	suite = unittest.TestSuite()
	suite.addTests( unittest.makeSuite( TestSudokuBoard ) )
	return suite


if __name__=="__main__":
	unittest.main()
