#!/usr/bin/python
# sudokuboard.py
#########################################
# This holds a complete 9x9 board
# 

import os

class SudokuBoard:
	baseBoard = []
	workBoard = []
	noteBoard = []    # notes for the board
	outType = "Full"
	outTypes = ["Full","Base","Work"]

	def __init__( self, size ):
		self.size = size
		self.vals = [str(val) for val in range(1,self.size+1)]
		self.clearBoard()
		
	def clearBoard( self ):
		self.baseBoard = [ [None]*self.size for i in range(self.size) ]
		self.resetBoard()
				
	def resetBoard( self ):
		""" sets workBoard to empty """
		self.workBoard = [[None for x in range(self.size)] for y in range(self.size)]
		self.noteBoard = [[[None for x in range(self.size)] for y in range(self.size)] for v in range(self.size)]
		
	def initBoard( self, strIn ):
		""" takes a comma delimited string to init the board """
		self.clearBoard()
		
		data = strIn.split(",")
		if len(data) != self.size * self.size:    # the correct size data should be given
			return
		for i in range( len( data ) ):
			if (data[i] == '') or (data[i] == ' '):
				data[i] = None
		for i in range( self.size ):
			row = data[0:self.size]
			data = data[self.size:]
			self.baseBoard[i]=row
	
	def loadFromFile(self,filename):
		""" load base data from filename """
		self.clearBoard()
		
		fh = open(filename,"r")
		line = fh.readline().strip()
		self.initBoard( line )
		return line

	def getRow(self,rowNum=None):
		if (rowNum == None) or (rowNum not in range(self.size)):
			return None
		rowB = self.baseBoard[rowNum]
		rowW = self.workBoard[rowNum]
		return map(lambda b,w: (w or b), rowB, rowW)

	def getCol(self,colNum=None):
		if (colNum == None) or (colNum not in range(self.size)):
			return None
		colB = [self.baseBoard[row][colNum] for row in range(self.size)]
		colW = [self.workBoard[row][colNum] for row in range(self.size)]
		return map(lambda b,w: (w or b), colB, colW)

	def getSquare(self, startCol=None, startRow=None, size=None):
		"""Return a tuple of (2d array of the items in the square, list of items)
		NONE where values not given
		"""
		if (startCol not in range(self.size)) or (startRow not in range(self.size)):
			return None
		if (size not in range(1,self.size+1)):
			return None
		if ((max(startCol,startRow) + size)) not in range(1,self.size+1):
			return None
		outS, outR = [],[]
		for r in range(startRow,startRow+size):
			colB = self.baseBoard[r][startCol:startCol+size]
			colW = self.workBoard[r][startCol:startCol+size]
			
			outS.append(map(lambda b,w: (w or b), colB, colW))
			outR.extend(map(lambda b,w: (w or b), colB, colW))
		return (outS, outR)
		
	def getValue( self, x, y ):
		return self.getSquare( x, y, 1 )[1][0]

	def getNotes( self, x, y ):
		""" return the notes list for x,y, or None for fail """
		if (x not in range(self.size)) or (y not in range(self.size)):
			return None
		return self.noteBoard[y][x]
		
	def getPossible( self, x, y ):
		""" return the possible values for the box """
		if (x not in range(self.size)) or (y not in range(self.size)):
			return None
		if self.getValue( x, y ):
			#print "getPossible",x,y,"has a value."
			return None
		#print "getPossible",x,y,"has notes:", self.getNotes( x, y )
		return list( set(self.vals) - set(self.getNotes( x,y )))

	def setValue(self, x, y, value):
		""" set the value into the workBoard for x,y.  returns value set """
		if (x not in range(self.size)) or (y not in range(self.size)):
			return None
		value = int(value)
		if (value not in range(1,self.size+1)):
			return None
		if (self.baseBoard[y][x] not in [None]):
			return None
		self.workBoard[y][x] = str(value)
		self.clearNoteAt( x, y )
		return value

	def clearValue( self, x, y ):
		self.workBoard[y][x] = None
	
	def setNoteValue( self, x, y, value ):
		""" set the value into the Notes board for x,y.  returns value set """
		if (x not in range(self.size)) or (y not in range(self.size)):
			return None
		value = int(value)
		if (value not in range(1,self.size+1)):
			return None
		if (self.baseBoard[y][x]) or (self.workBoard[y][x]):
			return None
		self.noteBoard[y][x][value-1] = str(value)
		return value
		
	def setOutType( self, typeIn="Full" ):
		if typeIn not in self.outTypes:
			return None
		self.outType = typeIn
		return self.outType
		
	def clearNoteAt( self, x, y ):
		""" clear the note values at coordinates. does not return a value """
		if (x not in range(self.size)) or (y not in range(self.size)):
			return
		self.noteBoard[y][x] = [None]*self.size

	def solvedPerCent( self ):
		""" returns % complete """
		total,solved = 0,0
		for r in range(self.size):
			for c in range(self.size):
				total += 1
				ch = None
				ch = self.workBoard[r][c] or self.baseBoard[r][c]
				if ch: solved += 1
		solvedPerCent = (solved*100)/total
		return solvedPerCent

	def isSolved( self ):
		""" returns % complete or True is solved """
		solvedPerCent = self.solvedPerCent()
		if solvedPerCent == 100:
			return True
		return False
	
	def __str__(self):
		outS = []
		for r in range(self.size):
			if (r%3 == 0):
				outS.append("-"*22)
			rowS = []
			for c in range(self.size):
				if (c%3 == 0):
					rowS.append("|")
				ch = None
				if (self.outType in ["Work", "Full"]):
					ch = self.workBoard[r][c]
				if (self.outType in ["Base","Full"]):
					ch = (self.baseBoard[r][c] or ch)
				if (ch in ['',None]):
					ch = '_'
				rowS.append(ch)
				rowS.append(' ')
			rowS.append("|")
			outS.append("".join(rowS))
		outS.append("-"*22)
		return "\n".join(outS)
