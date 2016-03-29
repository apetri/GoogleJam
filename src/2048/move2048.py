import sys
import numpy as np

#Make a 2048 move in the right direction
def move(line,direction="right"):

	#############################################################
	#################Clean line from zeros#######################
	#############################################################

	#Temporary storage, to clean from zeros
	lineClean = np.zeros_like(line)

	if direction=="right":
		
		#Positional iterator
		pos = reversed(range(len(line)))
		#Line iterator
		lineIter = reversed(line)

	elif direction=="left":

		#Positional iterator
		pos = range(len(line)).__iter__()
		#Line iterator
		lineIter = line.__iter__()

	i = pos.next()
	el = lineIter.next()

	#Iterate
	while True:

		if el>0:
			lineClean[i] = el

			try:
				i = pos.next()
			except StopIteration:
				break

		try:
			el = lineIter.next()
		except StopIteration:
			break

	#####################################################################################
	#Once the line is cleaned from the intermediate zeros, we are ready to make the move#
	#####################################################################################

	#Line after the move
	newLine = np.zeros_like(line)

	if direction=="right":

		#Positional iterator
		pos = reversed(range(len(line)))
		#Line iterator
		lineIter = reversed(lineClean)

	elif direction=="left":

		#Positional iterator
		pos = range(len(line)).__iter__()
		#Line iterator
		lineIter = lineClean.__iter__()

	#Read the first 2 elements
	el1 = lineIter.next()
	el2 = lineIter.next()
	i = pos.next()

	#Iterate
	while True:

		if el1==el2:
			
			newLine[i] = 2*el1

			try:
				el1 = lineIter.next()
			except StopIteration:
				break

			try:
				el2 = lineIter.next()
			except StopIteration:
				i = pos.next()
				newLine[i] = el1
				break


		else:

			newLine[i] = el1
			el1 = el2

			try:
				el2 = lineIter.next()
			except StopIteration:
				i = pos.next()
				newLine[i] = el1
				break

		try:
			i = pos.next()
		except StopIteration:
			break


	#Return the line after the move
	return newLine


#Make a 2048 move on the entire board
def moveBoard(board,direction="right"):

	if direction in ["left","right"]:

		for row in range(board.shape[0]):
			board[row] = move(board[row],direction)

	elif direction in ["up","down"]:

		board = board.transpose()
		
		for row in range(board.shape[0]):

			if direction=="up":
				board[row] = move(board[row],"left")
			else:
				board[row] = move(board[row],"right")

		board = board.transpose()


	return board


#Main execution
if __name__=="__main__":

	#In/out files
	input_filename = sys.argv[1]
	output_filename = input_filename.replace(".in.",".out.")
	output = file(output_filename,"w")

	#Process input
	with open(input_filename,"r") as infile:

		#Read number of test cases
		nTest = int(infile.readline().rstrip("\n"))

		#Cycle over test cases
		for t in range(nTest):

			#Read board size and direction
			size,direction = infile.readline().rstrip("\n").split(" ")
			size = int(size)

			#Read in the board
			board = list()
			for l in range(size):
				line = infile.readline().rstrip("\n").split(" ")
				board.append([ int(n) for n in line ])

			#Convert in numpy format
			board = np.array(board)

			#Make the move
			board = moveBoard(board,direction)

			#Write the output board
			output.write("Case #{0}:\n".format(t+1))
			
			for i in range(size):
				for j in range(size):
					output.write("{0} ".format(board[i,j]))
				output.write("\n")

	#Close output
	output.close()

