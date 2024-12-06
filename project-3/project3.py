#
# I made this program in a small bit of time. Finished in around two days.
#
# All I can say about this project is the following: Screw if/else statements. DICTIONARIES > IF/ELSE! TUPLE > SET > LIST! #immutable gang
#
# With this, theres only 4 if/else statements. None of those if/else statements are executed while looping. Only before the calculations start.
#
# It would've been really cool for this project to loop infinitely (from left/right, up/down.)
# I may explore this option if I make the repo public (as long as all the materials of this project are GPL, MIT, or some other public licence.)
#
# It isn't the best thing here. The worst-case time complexity is something like O(N^3). Not exactly the fastest thing ever, but it is what it is.
#

import argparse  						# Used for parsing inputs.
from multiprocessing import Pool		# Used for multiprocessing functionality.

# PERSONAL LIBRARY:
import utils
# utils.rules: 			Defines the utils.rules (X,x,.,o,O)
# utils.cellToInt: 		Translate 'string' cell values into their 'int' variants.
# utils.intToCell: 		Translate 'int' cell values into their 'string' variants.
# utils.nodeSumCheck: 	Based on the area (NW,SW,NE,SE,N*,S*,*W,*E,**) the sum is calculated.

# DEFINING FUNCTIONS:
#--------------------------------------------------------
# I - specify in, out, amount of threads to be used in it
def parseInput():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', required=True, help="Input file")
	parser.add_argument('-o', required=True, help="Output file")
	parser.add_argument('-p', required=False, help="Number of threads (defaults to 1)", default=1)
	parser.add_argument('-I', required=False, help="DEBUG: Number of iterations (defaults to 100)", default=100) # This command is just for debugging.
	args = parser.parse_args()
	inputFile = args.i
	outputFile = args.o
	threadNum = args.p
	iterations = args.I
	return([inputFile,outputFile,threadNum,iterations])

#--------------------------------------------------------
# II - open the file and convert the contents to a matrix
def fileToMatrix(arguments):
	with open(arguments, "r") as inputFile:
		fileList = [item.rstrip() for item in inputFile.readlines()]
	fileRowW = len(fileList[0])
	fileRowH = len(fileList)
	matrixWhole = []
	for row in range(fileRowH):
		matrixRow = []
		for column in range(fileRowW):
			currentVal = fileList[row][column]
			matrixRow.append(utils.cellToInt[currentVal])
		matrixWhole.append(matrixRow)
	inputFile.close()
	return matrixWhole

#--------------------------------------------------------
# III - calculate the next iteration of the row provided.
def rowCalc(board,row,rowLen,colLen,rowDict,colDict):
	rowStorage = []
	rowZoneCheck = rowDict[row]
	for col in range(colLen):
		colZoneCheck = colDict[col]
		cellSum = 0
		for nodeSum in utils.nodeSumCheck[rowZoneCheck][colZoneCheck]: # Look at utils.rules.py to see how this works.
			rowSum = nodeSum[0]
			colSum = nodeSum[1]
			cellSum += board[row + rowSum][col + colSum] # Sums up all the values for each cell.
		cellNum = utils.rules[board[row][col]][cellSum] # Look at utils.rules.py to see how this works.
		rowStorage.append(cellNum)
	return(rowStorage)

#--------------------------------------------------------
# IV - do the calculations via multithreading on the cpu.
def boardCalcMulti(board,maxRow,maxCol,maxThread,rowDict,colDict): # MULTITHREADING USES POOL
	with Pool(processes=maxThread) as pool: # This allocates "maxThread" amount of threads to the pool.
		resultCol = [(board, row, maxRow, maxCol,rowDict,colDict) for row in range(maxRow)] # A new array of given inputs for each row is needed.
		# I could try finding a way to make it such that if a processes is already finished, it just goes onto the next board rather waiting for everything to finish.
		# In fact it could probably be done in 2 or 3 more lines. However, I think this is the best of what I'm getting
		resultRow = pool.starmap(rowCalc, resultCol) # The pool ends up calculating each row with the given inputs from "resultCol"
		newMat = [row for row in resultRow] # The results are put into a new matrix ...
		pool.close()
		pool.terminate()
		pool.join()
	return newMat # ... and then that matrix is returned.

def boardCalcSerial(board,maxRow,maxCol,rowDict,colDict): # SERIAL IS ONE LOOP
	newMat = [] # New empty board is created
	for row in range(maxRow): # Creates a range between 0 and maxRow
		newMat.append(rowCalc(board,row,maxRow,maxCol,rowDict,colDict)) # Append the new "row"'th row to newBoard
	return newMat # Once it's done, it gets returned.

#--------------------------------------------------------
# V - output to a file that the user provided in the arg
def matrixToFile(fileName,matrix):
	with open(str(fileName), 'w') as matrixData:
		for row in matrix:
			for column in row:
				matrixData.write(utils.intToCell[int(column)])
			matrixData.write('\n')
	matrixData.close()

#--------------------------------------------------------
# VI - generate a dictionary that makes the program fast.
def lenToDict(length): # gets a length, determines where each cell needs to sum for the next state in utils.nodeSumCheck.
	cacheDict = []
	for num in range(length):
		cacheList = []
		pres = 0
		if(num == 0): # IF STATEMENT NUMBER 1
			pres = -1
		if(num == length - 1): # IF STATEMENT NUMBER 2
			pres = 1
		cacheDict.append([num,pres])
	return(dict(cacheDict))

def createDict(row,col): # if rows are equal to the amount of columns, it only carries one calculation.
	if(row == col): # IF STATEMENT NUMBER 3
		rowList = lenToDict(row)
		colList = rowList
	else: # ELSE STATEMENT NUMBER 1
		rowList = lenToDict(row)
		colList = lenToDict(col)
	return(rowList,colList)

# CALLING FUNCTIONS:
#========================================================
# 1 - parse the settings from the user (if i provided it)
settings			= parseInput()		# Settings are parsed from beginning
sFileInput   		= settings[0] 		# Input file name
sFileOutput  		= settings[1] 		# Output file name
sThreadCount 		= int(settings[2]) 	# (Optional) Amount of threads provided
sIterCount	 		= int(settings[3])	# (DEBUG) Amount of iterations

#========================================================
# 2 - open the file (that was provided) if it is possible
gameBoard			= fileToMatrix(sFileInput)
rowNum 				= len(gameBoard)
colNum 				= len(gameBoard[0])

#=========================================================
# 3 - create a dictionary to speed up all the calculations
rowDict, colDict 	= createDict(rowNum, colNum)

#================================================================
# 4 - start the calculation without any of the if-else
if(sThreadCount == 1): # IF STATEMENT NUMBER 4
	print("SERIAL MODE ACTIVE")
	for i in range(sIterCount):
		gameBoard = boardCalcSerial(gameBoard,rowNum,colNum,rowDict,colDict)
else: # ELSE STATEMENT NUMBER 2
	print("MULTITHREADED MODE ACTIVE")
	# Subtract 1 from sThreadCount (or else the number of "python" processes will not be equal to the number of threads.)
	for i in range(sIterCount):
		gameBoard = boardCalcMulti(gameBoard,rowNum,colNum,(sThreadCount - 1),rowDict,colDict)

#========================================================
# 5 - print and export the information that was generated
matrixToFile(sFileOutput,gameBoard)
