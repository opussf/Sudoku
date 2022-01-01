#!/usr/bin/env python
""" $Id: MakeTestSudokuFiles.py 296 2010-02-20 22:17:51Z opus $ 
This creates TestSudokuFiles.py
"""

import os
import re

replacePat = re.compile("[.]|[-]")

fName = "TestSudokuFiles.py"
head = """#!/usr/bin/env python
import unittest
import solveSudoku
import sudokuboard

class TestSudokuFiles( unittest.TestCase ):
	def setUp( self ):
		self.board = sudokuboard.SudokuBoard(9)
		self.solve = solveSudoku.SolveSudoku( self.board )
	def printOutput( self ):
		self.solve.board.outType = "Base"
		freshBoard = str(self.solve.board).split("\\n")
		self.solve.board.outType = "Full"	
		doneBoard = str(self.solve.board).split("\\n")
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
			print "%s\t%s\t%s" % ( freshBoard[line], doneBoard[line], " | ".join(moveList[line]) )
		print "="*80
"""

test = """\tdef test_%(funName)s( self ):
		self.solve.board.loadFromFile("%(file)s")
		self.solve.solveBoard()
		if not self.solve.board.isSolved():
			print "%(file)s fails:"
			self.printOutput()
			self.fail("%(file)s can only be solved to " + str(self.solve.board.solvedPerCent()) + "%%")"""

foot = """
def suite():
	suite = unittest.TestSuite()
	suite.addTests( unittest.makeSuite( TestSolveSudoku ) )
	return suite
		
if __name__ == "__main__":
	unittest.main()"""

fLines = []
fLines.append(head)

for name in os.listdir("."):
	if (name[:6] == "puzzle") and (name[-4:] == ".txt"):
		vals = {}
		vals['file'] = name
		vals['funName'] = re.sub( replacePat, "_", name )
		fLines.append(test % vals)

fLines.append(foot)

open(fName,"w").write("\n".join(fLines))

from TestSudokuFiles import *
