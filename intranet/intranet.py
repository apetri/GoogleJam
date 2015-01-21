import sys

#Decide if two wires intersect

def intersectTwo(a1,b1,a2,b2):
	return (a1>a2)!=(b1>b2)

#Compute number of intersection in a list of wires

def intersectN(wires,n):

	intersections = 0

	for i in range(n):
		for j in range(i+1,n):
			if intersectTwo(wires[i][0],wires[i][1],wires[j][0],wires[j][1]):
				intersections = intersections + 1

	return intersections


#Main execution

if __name__=="__main__":

	input_filename = sys.argv[1]
	output_filename = input_filename.replace(".in.",".out.")

	output = file(output_filename,"w")

	#Process input case by case
	with open(input_filename,"r") as infile:

		#Read the number of test cases
		nTest = int(infile.readline().strip("\n"))

		#Process each test case
		for t in range(nTest):

			wires = list()
			nWires = int(infile.readline().strip("\n"))

			for w in range(nWires):
				wires.append([ int(h) for h in infile.readline().strip("\n").split(" ") ])

			#Compute intersections and write to output
			output.write("Case #{0}: {1}\n".format(t+1,intersectN(wires,nWires)))


	#Close
	output.close()