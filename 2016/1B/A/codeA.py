#!/usr/bin/env python
from __future__ import division
import sys


process = {

0 : {"spell" : "ZERO" , "lead" : "Z"} ,
1 : {"spell" : "ONE" , "lead" : "O"} ,
2 : {"spell" : "TWO" , "lead" : "W"} ,
3 : {"spell" : "THREE" , "lead" : "H"} ,
4 : {"spell" : "FOUR" , "lead" : "U"} ,
5 : {"spell" : "FIVE" , "lead" : "F"} ,
6 : {"spell" : "SIX" , "lead" : "X"} ,
7 : {"spell" : "SEVEN" , "lead" : "S"} ,
8 : {"spell" : "EIGHT" , "lead" : "G"} ,
9 : {"spell" : "NINE" , "lead" : "I"} ,

}

order = [0,2,8,4,6,7,3,5,1,9]

def phoneNumber(s):

	count = dict()
	digits = list()
	

	#Count letters
	for c in s:
		if c not in count:
			count[c] = 1
		else:
			count[c] += 1

	#Fill in digits table with deletions
	for d in order:
		lead = process[d]["lead"] 
		if lead in count:
			for n in range(count[lead]):
				digits.append(d)
				for s in process[d]["spell"]:
					count[s]-=1
	
	#Return
	digits.sort()
	return "".join(str(n) for n in digits)


#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")
getstringlist = lambda : line().split(" ")
getint = lambda : int(line())
getintlist = lambda : [ int(n) for n in line().split(" ") ]


def main():

	#Number of test cases
	ntest = getint()

	#Cycle over test cases
	for t in range(ntest):
		
		s = line()

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,phoneNumber(s)))

if __name__=="__main__":
	main()