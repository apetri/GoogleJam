import sys
import numpy as np

#Class handler of the tiles
class BigTile(object):

	def __init__(self,size):
		self.size = size
		self.available = dict()
		for logSize in range(int(np.floor(np.log2(size))+1)):
			self.available[logSize] = (size>>logSize)**2

	def cutSmallTile(self,tileLogSize):
		for logSize in range(tileLogSize+1):
			self.available[logSize] -= 2**(2*(tileLogSize - logSize))


#Given a sequence of logSizes compute how many BigTiles are necessary to accomodate them all
def neededTiles(sequence,size):

	#First sort the sequence for convenience
	sequence.sort()

	#Create a list with only 1 tile
	tileList = [ BigTile(size) ]

	#Cut one tile at a time, starting from the bigger ones
	while True:

		cut = False

		try:
			logSize = sequence.pop()
		except IndexError:
			return len(tileList)

		#Try each of the BigTiles to see if there is available space
		for tile in tileList:
			if tile.available[logSize]:
				tile.cutSmallTile(logSize)
				cut = True
				break

		#If there is no space in the available tiles, we should buy another one
		if not(cut):
			newTile = BigTile(size)
			newTile.cutSmallTile(logSize)
			tileList.append(newTile)


#Main execution
if __name__=="__main__":

	#In/out filenames
	input_filename = sys.argv[1]
	output_filename = input_filename.replace(".in.",".out.")
	outfile = open(output_filename,"w")

	#Cycle over input lines
	with open(input_filename,"r") as infile:

		#Get number of test cases
		nTest = int(infile.readline().rstrip("\n"))

		#Cycle over test cases
		for t in range(nTest):

			#Read the entire input sequence
			sequence = [ int(n) for n in infile.readline().rstrip("\n").split(" ") ]

			#Number of tiles
			nTiles = sequence.pop(0)
			#Size of the tiles
			size = sequence.pop(0)

			#Compute the number of needed tiles
			needed = neededTiles(sequence,size)

			#Write the output
			outfile.write("Case #{0}: {1}\n".format(t+1,needed))


	#Close output
	outfile.close()
