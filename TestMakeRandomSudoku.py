#!/usr/bin/env python
from MakeRandomSudoku import *
import sudokuboard 

import os
import unittest

class TestMakeRandomSudoku( unittest.TestCase ):
	puzzleFile = "sudokuboard.puzzle.test"
	def validatePDFFile( self ):
		self.failUnless( os.path.exists( self.pdfFile ) )

	def setUp( self ):
		self.board=sudokuboard.SudokuBoard(9)
		self.rand = MakeRandomSudoku( self.board )
		self.board, self.fName = self.rand.generate()
	def test_MakeRandomSudoku_generate( self ):
		self.assert_( self.board.solvedPerCent() < 50 )    # greater than 50% is too easy?
	def test_MakeRandomSudoku_generatePDF_fromFileName( self ):
		self.pdfFile = self.rand.generatePDF( self.fName )
		self.validatePDFFile()
	def test_MakeRandomSudoku_generatePDF_fromFileName_noPreGen( self ):
		board = sudokuboard.SudokuBoard(9)
		rand = MakeRandomSudoku( board )
		self.pdfFile = rand.generatePDF( self.puzzleFile )
		self.validatePDFFile()
	def test_MakeRandomSudoku_generatePDF_fromObjectBoard( self ):
		self.pdfFile = self.rand.generatePDF()
		self.validatePDFFile()
	def test_MakeRandomSudoku_generatePDF_fromObjectBoard_noData( self ):
		board = sudokuboard.SudokuBoard(9)
		rand = MakeRandomSudoku( board )
		self.pdfFile = rand.generatePDF()
		self.assertEquals( self.pdfFile, None )    # only need to make sure that None is returned
	def test_MakeRandomSudoku_generatePDF_fileExists( self ):
		self.pdfFile = self.rand.generatePDF( self.fName )
		self.validatePDFFile()

def suite():
	suite = unittest.TestSuite()
	suite.addTests( unittest.makeSuite( TestMakeRandomSudoku ) )
	return suite
		
if __name__ == "__main__":
	unittest.main()
