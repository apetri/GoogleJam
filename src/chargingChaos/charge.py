#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

#Solve the problem for N odd
def chargeOdd(N,L,outlets,devices):

	#Initialize
	device_values = np.zeros(N,dtype=np.int)
	outlet_values = np.zeros(N,dtype=np.int)
	switch = 0

	#Switch mask
	mask = np.ones(N,dtype=np.int)

	#Check column sum, update device values
	for p in range(L):

		outlet_sum = outlets[:,p].sum()
		device_sum = devices[:,p].sum()
		device_values += devices[:,p]*(2**p)
		
		if outlet_sum==device_sum:
			outlet_values += outlets[:,p]*(2**p)
		
		elif outlet_sum==N-device_sum:
			switch += 1
			outlet_values += (outlets[:,p]^mask)*(2**p)

		else:
			return None

	#Match each device to its outlet
	device_values = set(device_values)
	for ov in outlet_values:
		if ov not in device_values:
			return None

	return switch

#Solve the problem for N generic
def charge(N,L,outlets,devices):
	
	if N%2:
		return chargeOdd(N,L,outlets,devices)

	new_devices = np.vstack((devices,devices[-1]))
	min_switch = L+1
	for n in range(N):
		
		new_outlets = np.vstack((outlets,outlets[n]))
		switch = chargeOdd(N+1,L,new_outlets,new_devices)
		
		if switch is not None and switch<min_switch:
			min_switch=switch

	if min_switch==L+1:
		return None
	else:
		return min_switch

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")
getstring = lambda : line()
getint = lambda : int(line())
getintlist = lambda : [ int(n) for n in line().split(" ") ]


def main():

	#Number of test cases
	ntest = getint()

	#Cycle over test cases
	for t in range(ntest):
		
		#Read N,L
		N,L = getintlist()
		devices = np.zeros((N,L),dtype=np.int)
		outlets = np.zeros_like(devices)

		#Read in outlets and devices
		for n,o in enumerate(line().split(" ")):
			outlets[n] = np.array([int(b) for b in o])

		for n,d in enumerate(line().split(" ")):
			devices[n] = np.array([int(b) for b in d])

		answer = charge(N,L,outlets,devices)
		if answer is None:
			answer = "NOT POSSIBLE"

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,answer))

if __name__=="__main__":
	main()