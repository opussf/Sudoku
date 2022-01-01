#!/usr/bin/python

import solveSudoku
import sudokuboard
import sys

puzzle = ['']*81
board = sudokuboard.SudokuBoard(9)
solveBoard = solveSudoku.SolveSudoku()
showMoves, showMovesNum = True, 5

def enterData():
	global puzzle
	global solveBoard
	global showMoves, showMovesNum
	done = False
	offset = 0
	while not done:
		c = raw_input(">").lower()
		if not len(c):
			print ">%s<" % ("".join(puzzle),)
			#print "Enter something idiot"
			#continue
		elif c[0] == "d":
			puzzle[offset-1]=''
			offset -= 1
			pStr = ",".join(puzzle)
			board.initBoard(pStr)
		elif c[0] == "c":
			offset = 0
			puzzle=['']*81
			pStr = ",".join(puzzle)
			board.initBoard(pStr)
		elif c[0] == "s":
			fname = getFilename()
			saveData( fname )
		elif c[0] == "l":
			fname = getFilename()
			loadData( fname )
			#solveBoard.setBoard(board)
			offset = (9*9) -1
		elif c[0] == "m":
			if len(c)>1:
				showMovesNum = int(c[1:])
			else:
				showMoves = not showMoves	
			if not showMoves: print "Not",
			print "Showing %i columns of moves" % showMovesNum
			continue
		elif c[0] == "n" and len(c)==3:
			solveBoard.solveBoard()
			x, y = int(c[1]), int(c[2])
			print x,y, solveBoard.board.getNotes( x, y )
			continue
		elif c[0] == "p" and len(c)==3:
			solveBoard.solveBoard()
			x, y = int(c[1]), int(c[2])
			notes = solveBoard.board.getNotes( x, y )
			print list( set(board.vals) - set(notes) )
			continue
		else:
			chars = list(c)
			chars = map( xFilter, chars )
			puzzle[offset:offset+len(chars)] = chars
			offset += len(chars)
			
		pStr = ",".join(puzzle)
		board.initBoard(pStr)
		solveBoard.setBoard(board)
		solveBoard.solveBoard()
		printBoard()
		
def xFilter( x ):
	if x in ['1','2','3','4','5','6','7','8','9']:
		return x
	else:
		return ' '

def printBoard():
	global showMoves, showMovesNum
	#print "Boards"
	solveBoard.board.outType = "Base"
	freshBoard = str(solveBoard.board).split("\n")
	solveBoard.board.outType = "Full"
	emptyPerCent = solveBoard.board.solvedPerCent()		
	doneBoard = str(solveBoard.board).split("\n")
	# build moveList for printing

	moves = [["%s %s %i,%i" % (m[2],m[3],m[0],m[1])] for m in solveBoard.getAllMoves()]
	#print moves
	
	moveList = [[] for i in range(13)]
	if showMoves:	
		line,mc = 0, 0
		for m in moves:
			if line >= 13:
				continue
			moveList[line].extend(m)
			mc += 1
			if mc >= showMovesNum:
				line, mc = line+1, 0
		
	for line in range(len(freshBoard)):
		print "%s\t%s\t%s" % ( freshBoard[line], doneBoard[line], " | ".join(moveList[line]) )
	print "%i%%\t\t\t%i%%  %0.3fs Moves: %i" % \
			(emptyPerCent, solveBoard.board.solvedPerCent(), solveBoard.getSolveTime(),len(solveBoard.getAllMoves()))
	
def getFilename():
	fname = raw_input("Please enter filename:")
	return fname
				
def saveData( fname ):
	pStr = ",".join(puzzle)
	file(fname,"w").write(pStr)
	
def loadData( fname ):
	global puzzle
	puzzle = board.loadFromFile(fname)
	puzzle = puzzle.split(",")
	puzzle = map( lambda x: x=='' and ' ' or x, puzzle )
	puzzle = "".join(puzzle)
	solveBoard.setBoard(board)
	#solveBoard.solveBoard()
	return board

def main():
	print board
	enterData()
	
if __name__ == "__main__":
	print sys.argv
	if len(sys.argv) > 1:
		loadData( sys.argv[1] )
	main()
