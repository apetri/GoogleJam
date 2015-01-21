import sys
from bitarray import bitarray

#Build a hash table with the 7-bit representations of each of the integers
bits = dict()
bits[0] = bitarray("1111110")
bits[1] = bitarray("0110000")
bits[2] = bitarray("1101101")
bits[3] = bitarray("1111001")
bits[4] = bitarray("0110011")
bits[5] = bitarray("1011011")
bits[6] = bitarray("1011111")
bits[7] = bitarray("1110000")
bits[8] = bitarray("1111111")
bits[9] = bitarray("1111011")

#Decide when an observation is compatible with a certain digit
def compatible(observation,digit):

	if (observation&(~bits[digit])).any():
		return False
	else:
		return True


#Given a string of 7 bits, decide which are the possible candidate digits
def candidateDigits(s):

	s_bits = bitarray(s)
	candidates = list()
	
	for i in range(10):
		if compatible(s_bits,i):
			candidates.append(i)

	return candidates

#Check if the digit is a good candidate to initiate the sequence
def goodCandidate(digit,sequence):

	##########################################################
	#We need to keep track of the info if a LED is down or up#
	##########################################################

	#This is 1 for the working LEDs and 0 for the unknown ones 
	on = bitarray(sequence[0])
	#This is 1 for the broken LEDs and 0 for the unknown ones
	off = bits[digit]^bitarray(sequence[0])

	##########################################################

	while len(sequence)>0:
		
		if digit in candidateDigits(sequence[0]):

			#Check for contradictions
			if (on&off).any():
				return -1

			on = on | bitarray(sequence[0])
			off = off | (bits[digit]^bitarray(sequence[0]))

			#Go to next element
			sequence = sequence[1:]
			digit = (digit - 1)%10
		
		else:
			return -1

	#Check for contradictions
	if (on&off).any():
		return -1

	#Fail if a LED with undefined state is on
	if ((~(on|off))&bits[digit]).any():
		return 1

	#Otherwise return the LEDs corresponding to the next digit, taking into account the broken ones
	return (bits[digit]&(~off)).to01()


#Process a sequence
def next(sequence):

	#Skip some work: if the sequence is longer or equal to 10, take advantage of periodicity
	if len(sequence)>=10:
		return sequence[len(sequence)%10]

	candidates = set()
	firstDigit = candidateDigits(sequence[0])

	for digit in firstDigit:
		
		candidate = goodCandidate(digit,sequence)

		if candidate==1:
			return "ERROR!"
		
		if candidate!=-1:
			candidates.add(candidate)

		if len(candidates)>1:
			return "ERROR!"

	if len(candidates):
		return candidates.pop()
	else:
		return "NONE!"


#Main execution
if __name__=="__main__":

	#Usual I/O
	input_filename = sys.argv[1]
	output_filename = input_filename.replace(".in.",".out.")
	output = file(output_filename,"w")

	#Cycle over input
	with open(input_filename,"r") as infile:

		#Read number of test cases
		nTest = int(infile.readline().rstrip("\n"))

		#Cycle over test cases
		for t in range(nTest):

			#Read digit sequence
			sequence = infile.readline().rstrip("\n").split(" ")[1:]

			#Compute the next element in the sequence and record it in the output
			output.write("Case #{0}: {1}\n".format(t+1,next(sequence)))


	#Close output
	output.close()


