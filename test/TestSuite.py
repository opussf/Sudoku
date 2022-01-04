#!/usr/bin/env python
import unittest
import xmlrunner
from TestSolveSudoku import *
from TestSudokuboard import *
from TestSudokuFiles import *
from TestMakeRandomSudoku import *

suite = unittest.TestSuite()
#suite.addTests( unittest.makeSuite( TestSudokuBoard ) )
suite.addTests( unittest.makeSuite( TestSolveSudoku ) )
#suite.addTests( unittest.makeSuite( TestSudokuFiles ) )
#suite.addTests( unittest.makeSuite( TestMakeRandomSudoku ) )

if __name__=="__main__":
	testsRan = xmlrunner.XMLTestRunner().run( suite )
	exit( len( testsRan.failures ) + len( testsRan.errors ) )
