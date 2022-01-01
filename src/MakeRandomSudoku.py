""" $Id$
"""

import time
import random
import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch, pica
import sudokuboard
import solveSudoku

class MakeRandomSudoku( solveSudoku.SolveSudoku ):
	""" Generate a random Sudoku board.
	Method:  Use the possible set returned for any one box, randomly choose, move on.
	"""
	fName = None
	def __init__( self, board ):
		super(MakeRandomSudoku,self).__init__( )
		self.setBoard( board )
	def generate( self ):
		""" returns the board, and the filename """
		self.fName = "puzzle-%i.txt" % ( int( time.time() ), )
		y,lc,uc = 0,0,0    # y, loopCounter, utimateCounter
		while y <= 8:
			if (self.makeRandomRow( y )):
				y,lc = y+1,0
				#print self.board
			else:
				lc,uc = lc+1, uc+1
				self.buildUsedAll()
			if lc>20 and y>1:
				self.clearRow(y)
				self.clearRow(y-1)
				self.clearRow(y-2)
				y,lc = y-2,0
				self.buildUsedAll()
			if uc>2000:
				return None
		print self.board
		self.pokeHoles()
		return (self.board, self.fName)
	def clearRow( self, y ):
		for x in range(9):
			self.board.clearValue( x, y )
	def makeRandomRow( self, y ):
		used = []
		try:
			for x in range(9):
				possible = self.board.getPossible( x, y )
				#print x,y, possible
				rVal = possible[random.randint(0,len(possible)-1)]
				self.board.setValue( x, y, rVal )
				self.buildUsedAll()
			return True
		except ValueError:
			for x in range(9):
				self.board.clearValue( x, y )
			return None
	def getPuzzleList( self ):
		""" returns a list that defines a puzzle.  Can be used to write out to the file.
		Filters None to ''
		"""
		puzzleOut = []
		for y in range(9):
			puzzleOut.extend( self.board.getRow( y ) )
		puzzleOut = map( lambda x: x or '', puzzleOut )
		return puzzleOut
	def pokeHoles( self ):
		""" This randomly removes values from the board """
		#print "PokeHoles"
		puzzleList = self.getPuzzleList()
		lcv = 45
		while lcv:
			x = random.randint(0,8)
			y = random.randint(0,8)
			offset = (y*9)+x
			if puzzleList[offset] != '':
				puzzleList[offset] = ''
				lcv-=1
		
		canSolve = True
		while canSolve:
			remove = True
			while remove:
				x = random.randint(0,8)
				y = random.randint(0,8)
				offset = (y*7)+x
				if puzzleList[offset] != '':
					puzzleList[offset] = ''
					remove = False
			self.board.initBoard( ",".join( puzzleList ) )
			self.solveBoard()
			canSolve = self.board.isSolved()
		#print "End of PokeHoles.  Saving...."
		self.board.initBoard( ",".join( puzzleList ) )
		self.saveBoard( puzzleList )
		
	def saveBoard( self, puzzleList = None ):
		if not puzzleList:
			puzzleList = self.getPuzzleList()
		file( self.fName, "w" ).write( ",".join( puzzleList ) )
		
	def generatePDF( self, fname = None ):
		""" Generate a PDF of a puzzle in a file.
		Writes the pdf and returns the fileName """
		print fname, self.fName
		
		board = self.board
		if not fname:
			if not self.fName:
				return None
			fname = self.fName
		else:
			board = sudokuboard.SudokuBoard(9)
			board.loadFromFile( fname )
		print board
		
		puzzleName = os.path.splitext( fname )[0]
		pdfFile = puzzleName + ".pdf" 
		print "pdfFile",pdfFile
		
		LINEWIDTH = 0.05 * inch
		boxSize = 0.5    # in inches
		
		pdf = Canvas( pdfFile, pagesize=letter, bottomup=0 )
		width, height = letter
		
		pdf.setStrokeColorRGB(0, 0, 0)    # black
		pdf.setFillColorRGB(0, 0, 0)
		
		# puzzle Title
		pdf.setFont( "Courier", 12 )
		pdf.drawCentredString( width/2, inch, puzzleName )
		
		#Draw the box
		pdf.setLineWidth( LINEWIDTH )
		pdf.translate( (width/2)-(9*boxSize*inch/2), 1.5*inch )
		
		# vertical rectangles
		pdf.rect( 0, 0, 3*boxSize*inch, 9*boxSize*inch )
		pdf.rect( 3*boxSize*inch, 0, 3*boxSize*inch, 9*boxSize*inch )
		pdf.rect( 6*boxSize*inch, 0, 3*boxSize*inch, 9*boxSize*inch )
		
		# horitonzal
		pdf.rect( 0, 0, 9*boxSize*inch, 3*boxSize*inch )
		pdf.rect( 0, 3*boxSize*inch, 9*boxSize*inch, 3*boxSize*inch )
		pdf.rect( 0, 6*boxSize*inch, 9*boxSize*inch, 3*boxSize*inch )
			
		pdf.setLineWidth( LINEWIDTH / 3 )
		for x in range(10):
			pdf.line( x*boxSize*inch, 0, x*boxSize*inch, 9*boxSize*inch)
			pdf.line( 0, x*boxSize*inch, 9*boxSize*inch, x*boxSize*inch)
		
		# Print the values
		pdf.setFont( "Courier", 48*boxSize )
		for y in range(9):
			py = ((y*boxSize)+(boxSize*0.7))*inch
			for x in range(9):
				val = board.getValue( x, y )
				if val:
					pdf.drawCentredString( ((x*boxSize)+(boxSize/2))*inch, py, val )
		
		
		
		pdf.showPage()
		pdf.save()
		
		
		return pdfFile
