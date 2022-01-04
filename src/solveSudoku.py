#!/usr/bin/python
# solveSudoku.py
#########################################
# This drives the solving of a sudoku puzzle
#

import sudokuboard
import time

class SolveSudoku( object ):
	board = None
	allMoves = None
	solveTime = None
	
	def __init__( self, board = None ):
		self.size = 9
		self.squareSize = 3
		#self.vals = [str(val) for val in range(1,self.size+1)]
		self.setBoard( board )
		
	def setBoard( self, board ):
		self.board = board
		self.lpCount = 0
		
	def getAllMoves( self ):
		return self.allMoves
		
	def getSolveTime( self ):
		return self.solveTime

	def solveLine(self,line):
		"""Solve a single line.  This can be a column, or row, but must be the size of the puzzle
		Mostly will just find singles that are missing as there is no other data available to it
		returns the modified line, and a tuple of (pos, value)
		"""
		missing = filter(lambda x: x in line, self.board.vals)
		missing = [val for val in self.board.vals if val not in line]
		if len(missing) == 1:
			pos = line.index(None)
			line[pos] = missing[0]
			return (line, (pos, missing[0]))
		return None

	def solveSquare( self, square ):
		""" Square is a list of lists that represent a square
		returns the modified square and a tuple: ( (x,y), value) 
		Note really needed?
		"""
		
		# Convert to a line, and try solveLine first
		line = []
		for r in square:
			line.extend(r)
		#print self.solveLine( line )

		return None
		
	def buildUsed( self, x, y ):
		""" Builds a used set for a square.  Used set is values that the square cannot be,
		and can be recorded into the notes part of the board.
		Pulls values from the square, column and row for that square.
		returns none if already set
		"""
		if (self.board.getValue( x, y )):
			return self.board.getNotes( x, y )
		self.board.clearNoteAt( x, y )
		# find the upper left of the square for this point
		squareX = (x / self.squareSize) * self.squareSize
		squareY = (y / self.squareSize) * self.squareSize
		
		# search column for values and set in the Notes
		for val in self.board.getCol( x ):
			if val:
				self.board.setNoteValue( x, y, val )
		
		# search row for values and set in the Notes
		for val in self.board.getRow( y ):
			if val:
				self.board.setNoteValue( x, y, val )

		# search square for values and set in the Notes
		for val in self.board.getSquare( squareX, squareY, self.squareSize )[1]:
			if val:
				self.board.setNoteValue( x, y, val )
		return self.board.getNotes( x, y )
				
	def buildUsedAll( self ):
#		print "buildUsedAll()"
		for y in range(self.size):
			for x in range(self.size):
				self.buildUsed( x, y )

	def solveForSingleValues( self ):   # sv
		""" This finds any box that has a single value available to it, and assigns that value.
		Loop until no more single values are found
		This solves any line, row, or even square
		returns a list of 'moves', (x, y, value)
		(Bottom right)
		"""
		moves = []
		repeat = True
		loopCount = 0
		while repeat:
			repeat = False
			for y in range(self.size):
				for x in range(self.size):
					#self.buildUsed( x, y )
					singleMissing = self.solveLine( self.board.getNotes( x, y ) )
					if singleMissing:
						self.board.setValue( x, y, singleMissing[1][1] )
						moves.append( (x, y, singleMissing[1][1], "sv") )
						#print x,y, singleMissing[1][1], "SingleValue"
						#print self.board
						repeat = True
			if repeat: 
				loopCount += 1
		return moves
	
	def solveForSingleMissing( self ):  # sm
		""" This finds any box in the square where it can only have 1 value.
		This is where a cross test finds a single box in a square can have a value.
		Also finds rows or columns in a square that can only have a value, and marks the rest of the row or column as such
		(bottom left)
		"""
		moves = []
		repeat = True
		loopCount = 0
		while repeat:
			repeat = False
			squareVals = range( 0, self.size, self.squareSize )
			# loop through the squares
			for sY in squareVals:
				for sX in squareVals:
					#print "\tSquare starting at:",sX, sY
					lists = []
					# loop through the boxes in the square.  
					for y in range(sY, sY+3):
						for x in range(sX, sX+3):
							self.buildUsed( x, y )
							cannotBeList = self.board.getNotes( x, y )    # ['1',None,'3'
							#print cannotBeList
							cannotBeList = filter( lambda x: x, cannotBeList)
							if len(cannotBeList):
								lists.append([x,y,cannotBeList])
						
					missing = {}
					for v in self.board.vals:
						cols, rows = {}, {}
						notFoundCount = 0
						for e in lists:
							if v not in e[2]:
								notFoundCount += 1
								#print v, "not found at:",e[0],e[1]
								missing[v] = [e[0],e[1]]
								cols[e[0]] = e[1]
								rows[e[1]] = e[0]
						if len(cols) == 1:
							x = cols.keys()[0]
							#print v, "can only fit in column", x, "in this square"
							#print "mark in notes for rows", set(range(self.size)).difference(set(rows.keys()))
							for y in range(self.size):
								if y not in rows.keys():
									self.board.setNoteValue( x, y, v )
						if len(rows) == 1:
							y = rows.keys()[0]
							#print v, "can only fit in row", y, "in this square"
							#print "mark in notes for columns", set(range(self.size)).difference(set(cols.keys()))
							for x in range(self.size):
								if x not in cols.keys():
									self.board.setNoteValue( x, y, v )
						
						if notFoundCount == 1:
							#print v, "was not found only once"
							#print v, "should go at", missing[v]
							x, y = missing[v]
							moves.append( ( x, y, v, "sm" ) )
							self.board.setValue( x, y, v )
							repeat = True
			if repeat: 
				loopCount += 1
				#print "Loop"
		return moves
		
	def solveForHiddenSingle( self ):   # hs
		""" http://angusj.com/sudoku/hints.php
		find a hidden single - a value that can only be in one location in a set 
		search the notes (possible values) for a single box with a unique possible value
		"""
		for x in range( self.board.size ):
			missingValsPos = {}    # How many times the missing values are found in this col
			for y in range( self.board.size ):
				possibleVals = self.board.getPossible( x, y )    # list of possible values
				#print x, y, possibleVals, self.board.getValue( x, y )
				if possibleVals:    # if not None
					for possVal in possibleVals:
						if possVal in missingValsPos.keys():    # assign 
							missingValsPos[possVal].append(y)
						else:
							missingValsPos[possVal] = [y]
			for val, yVals in missingValsPos.items():    # find values with a single location
				if len(yVals) == 1:
					#print "HiddenSingle:",val,"Should go at:",x,yVals[0], "Cols"
					self.board.setValue( x, yVals[0], val )
					#self.buildUsedAll()
					return [ (x, yVals[0], val, "hs")]
		for y in range( self.board.size ):
			missingValsPos = {}    # How many times the missing values are found in this row
			for x in range( self.board.size ):
				possibleVals = self.board.getPossible( x, y )
				if possibleVals:
					#print x, y, possibleVals
					for possVal in possibleVals:
						if possVal in missingValsPos.keys():
							missingValsPos[possVal].append(x)
						else:
							missingValsPos[possVal] = [x]
			for val, xVals in missingValsPos.items():
				if len(xVals) == 1:
					#print "HiddenSingle:",val,"Should go at:",xVals[0],y, "Rows"
					self.board.setValue( xVals[0], y, val )
					#self.buildUsedAll()
					return [(xVals[0], y, val, "hs")]
			#print "="*42
		return []
		
	def solveForDirectInteraction( self ):  # di
		""" direct interaction
		This is where a value is only possible in a single row or column in a square.
		That condition removes that value from all other locations in that row or column
		"""

		moves = []
		squares = range( 0, self.size, self.squareSize )
		# loop through the squares
		for sY in squares:
			for sX in squares:
				#print "\tSquare starting at:",sX, sY
				squareValues = self.board.getSquare( sX, sY, self.squareSize )
				# find missing values
				for v in self.board.vals:
					missingIn = [[],[]] # [[columns], [rows]]
					if v not in squareValues[1]:   # v is missing from this square
						for y in range( sY, sY+self.squareSize ):
							for x in range( sX, sX+self.squareSize ):
								possibleAt = self.board.getPossible( x, y )  # get the possible value for each coord
								if possibleAt and v in possibleAt:
									missingIn[0].append(x)
									missingIn[1].append(y)
									#print("%s: %s" % (v,missingIn))
						# done finding, remove duplicates   [5,5,5] -> [5], [4,5] -> [4,5]
						missingIn[0] = list(set(missingIn[0]))
						missingIn[1] = list(set(missingIn[1]))
						#print( v, missingIn )
						if len( missingIn[0] ) == 1:
							singleColumn = missingIn[0][0]
							print( "\t%s can only be in column %s in Square (%s,%s)." % (v, singleColumn, sX, sY ) )
							for y in list(set(range(self.size)) - set(range( sY, sY+self.squareSize))):
								#print(self.board.getPossible( singleColumn, y ) )

								if self.board.setNoteValue( singleColumn, y, v ):
									print( "SetNoteValue( %s, %s, %s )" % (singleColumn, y, v))
									moves.append([singleColumn, y, v, "di"])
		"""
					if v in missingIn.keys():
						missingIn[v][0] = list(set(missingIn[v][0]))
						missingIn[v][1] = list(set(missingIn[v][1]))
						print( v, missingIn[v] )

						if len(missingIn[v][0]) == 1:
							singleColumn = missingIn[v][0][0]
							print( "%s can only be in column %s in Square (%s,%s)." % (v, singleColumn, sX, sY ) )
							#print("%s can only be in column %s" % (v,singleColumn) )
							#print( list(set(range(self.size)) - set(range( sY, sY+self.squareSize))))
							for y in list(set(range(self.size)) - set(range( sY, sY+self.squareSize))):
								if self.board.clearNoteValue( singleColumn, y, v ):
									moves.append([singleColumn, y, v, "di"])

						elif len(missingIn[v][1]) == 1:
							singleRow = missingIn[v][1][0]
							print("%s can only be in row %s" % (v,singleRow))
							for x in list(set(range(self.size)) - set(range( sX, sX+self.squareSize))):
								if self.board.clearNoteValue( x, singleRow, v ):
									moves.append([x, singleRow, v, "di"])
		"""


		return moves


#	def solveForDoubleMissingValues( self ):
#		""" Find places where a box has to be a value because of double elimination.
#		find any row or column with only 2 values missing.
#		-> same square, clear whole col / row
#		-> diff square, clear col / row for only in square
#		"""
#		for x in range(self.size):
#			col = self.board.getCol( x )
#			missingCount = len( filter( lambda x: not x, col ) )
#			if missingCount >= 2:
#				print missingCount, "col:",x, col
#				for y in range(self.size):
#					if not col[y]:
#						print x,y, self.board.getNotes(x,y) 
#		for y in range(self.size):
#			row = self.board.getRow( y )
#			missingCount = len( filter( lambda x: not x, row ) )
#			if missingCount >= 2:
#				print missingCount, "row:",y, row
#				for x in range(self.size):
#					if not row[x]:
#						print x,y, self.board.getNotes(x,y)
#		return []
		
	def eliminateLockedPairValues( self, ver ):
		""" Eliminate Locked Pair Values from Notes 
		ver should be in [1,2,3] 1 for column testing, 2 for row testing, 3 for square"""
		#self.buildUsedAll()
		valOut = []
		lpList = []    # list of boxes to mark [x,y,val]
		# columns
		if ver == 1:
			for x in range( self.size ):
				lockedPairs = []
				lockedPair = None
				for y in range( self.size ):
					possibleVals = self.board.getPossible( x, y )
					if possibleVals and len( possibleVals ) == 2:
						if possibleVals in lockedPairs:
							lockedPair = possibleVals
						lockedPairs.append( possibleVals )
				if lockedPair:
					#print "Found locked pair:", lockedPair, "in col:", x
					valOut.append([x,9,'c','lp'])
					for y in range( self.size ):
						for v in lockedPair:
							lpList.append([x,y,v])
		# rows
		elif ver == 2:
			for y in range( self.size ):
				lockedPairs = []
				lockedPair = None
				for x in range( self.size ):
					possibleVals = self.board.getPossible( x, y )
					if possibleVals and len( possibleVals ) == 2:
						if possibleVals in lockedPairs:
							lockedPair = possibleVals
						lockedPairs.append( possibleVals )
				if lockedPair:
					#print "Found locked pair:", lockedPair, "in row:", y
					valOut.append([9,y,'r','lp'])
					for x in range( self.size ):
						for v in lockedPair:
							lpList.append([x,y,v])
		# work through squares
		elif ver == 3:
			for xx in range( 0, self.size, 3 ):
				for yy in range( 0, self.size, 3 ):
					squareCoords = []
					for x in range( xx, xx+3 ):
						for y in range( yy, yy+3 ):
							squareCoords.append([x,y])
					lockedPairs = []
					lockedPair = None
					for x,y in squareCoords:
						possibleVals = self.board.getPossible( x, y )
						if possibleVals and len( possibleVals ) == 2:
							if possibleVals in lockedPairs:
								lockedPair = possibleVals
							lockedPairs.append( possibleVals )
					if lockedPair:
						#print "Found locked pair:", lockedPair, "in square:", xx,yy
						valOut.append([xx,yy,'s','lp'])
						for x,y in squareCoords:
							for v in lockedPair:
								lpList.append([x,y,v])
		for x,y,v in lpList:
			self.board.setNoteValue( x, y, v )
			#print x,y,v, self.board.getNotes( x, y )
		return valOut
		
	def solveSingle5050( self ):
		""" Solve a 50/50 split """
		# has 5050 been called before?
		calledTimes = len( filter( lambda x: x[3]=='ff', self.allMoves ) )
		#skipCount = calledTimes / 2
		reverse = calledTimes % 2
		if reverse:
			reverseVals = filter( lambda x: x[3]=='ff', self.allMoves )[-1]
			revert = True
			while revert:
				revertVal = self.allMoves.pop()
				if revertVal[3] != 'lp':
					#print "revertVal", revertVal
					self.board.clearValue( *revertVal[:2] )
					if revertVal[3] == 'ff':
						revert = False
						self.allMoves.append(revertVal)
					
			self.buildUsedAll()
			val = list( set(self.board.getPossible( *revertVal[:2] )) - set(revertVal[2]) )[0]
			self.board.setValue( revertVal[0], revertVal[1],  val )
			self.buildUsedAll()
			return [ (revertVal[0], revertVal[1], val, "ff") ]
			
			
		#print "5050", calledTimes, skipCount, reverse, self.allMoves
		# find a box with 2 possible values
		for y in range( self.board.size ):
			for x in range( self.board.size ):
				possVals = self.board.getPossible( x, y )
				if possVals and (len( possVals ) == 2):
					val = possVals[0]
					self.board.setValue( x, y, val )
					self.buildUsedAll()
					return [ (x, y, val, "ff") ]
		return []
		
	def solveBoard( self ):
		""" loop through the calls """
		#print self.board
		#print self.board.solvedPerCent()
		self.allMoves = []
		repeat = True
		start = time.clock()
		self.buildUsedAll()
		loopCount = 20
		lpToDo = 3
		while repeat and loopCount:
			loopMoves = 0
			loopCount -= 1
			repeat = False
			moves = self.solveForSingleValues()
			if len(moves) > 0: repeat,lpUsed = True,3
			self.allMoves.extend(moves)
			loopMoves += len(moves)
			
			moves = self.solveForSingleMissing()
			if len(moves) > 0: repeat,lpUsed = True,3
			self.allMoves.extend(moves)
			loopMoves += len(moves)
			
			"""
			if (loopMoves == 0):
				print "0 moves.  Solved:", self.board.isSolved(), self.board.solvedPerCent()
			"""

			if (loopMoves == 0) and not self.board.isSolved():
				moves = self.solveForHiddenSingle()
				self.buildUsedAll()
				#print "HiddenSinge moves:", moves
				self.allMoves.extend(moves)
				loopMoves += len(moves)
				if len(moves) > 0: repeat = True

			if (loopMoves == 0) and not self.board.isSolved():
				moves = self.solveForDirectInteraction()
				if len(moves) > 0: repeat = True
				self.allMoves.extend(moves)
				loopMoves += len(moves)
				
			if (loopMoves == 0) and (not self.board.isSolved()) and (lpToDo):
				#print "Trying Locked Pair elimination"
				moves = self.eliminateLockedPairValues(lpToDo)
				#if repeat: print "Locked Pair elimination found"
				self.allMoves.extend(moves)
				if lpToDo: 
					repeat = True
				lpToDo -= 1

			
			#if (loopMoves == 0) and (not self.board.isSolved()):
			#	moves = self.solveSingle5050()
			#	self.allMoves.extend(moves)
			#	if len(moves) > 0: repeat = True
			
			#moves = self.solveForDoubleMissingValues()
			#if len(moves) > 0: repeat = True
			#self.allMoves.extend(moves)

		#print "Loops:", loopCount
		end = time.clock()
		self.solveTime = end - start
		#self.buildUsedAll()
		#print self.solveTime
		#print moveCount, len(self.allMoves)
		return self.allMoves
