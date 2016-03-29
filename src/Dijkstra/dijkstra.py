#!/usr/bin/env python

from __future__ import division
import sys

tbl = dict()
tbl["1"] = ["1","i","j","k"]
tbl["i"] = ["i","-1","k","-j"]
tbl["j"] = ["j","-k","-1","i"]
tbl["k"] = ["k","j","-i","-1"]

p = dict()
p["1"] = 0
p["i"] = 1
p["j"] = 2
p["k"] = 3

#Multiply two quaternions
def mul(a,b):

	minus = 0
	minus += "-" in a
	minus += "-" in b

	result = tbl[a.strip("-")][p[b.strip("-")]]
	minus += "-" in result

	if minus%2:
		return "-"+result.strip("-")
	else:
		return result.strip("-")

#Find the answer of a particular test case
def possible(L,X,s):

	#Multiples of 4 cannot work
	if not X%4:
		return "NO"

	#Evaluate the string cumulatively up to 4 times
	i = -1
	k = -1
	times = min(X,4)

	s_evaluates_to = "1"
	for n in range(L*times):
		
		s_evaluates_to = mul(s_evaluates_to,s[n%L])
		
		if s_evaluates_to=="i" and i==-1:
			i=n

		if s_evaluates_to=="k":
			k=n

		if n==L-1:
			xs_evaluates_to = s_evaluates_to
			
			for t in range(X%4-1):
				xs_evaluates_to = mul(xs_evaluates_to,s_evaluates_to)

			if xs_evaluates_to!="-1":
				return "NO"

	if i==-1 or k==-1:
		return "NO"

	if i<k:
		return "YES"

	if 4*L+k<L*X:
		return "YES" 
	else:
		return "NO" 

#Main execution
if __name__=="__main__":

	input = sys.stdin
	output = sys.stdout

	T = int(input.readline().strip("\n"))
	for t in range(T):
		
		L,X = [ int(n) for n in input.readline().strip("\n").split(" ") ]
		s = input.readline().strip("\n")
		output.write("Case #{0}: {1}\n".format(t+1,possible(L,X,s)))






