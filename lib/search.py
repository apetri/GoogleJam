from __future__ import division

#####################################################################
####Binary search that falls one step short in finding the target####
#####################################################################

def binary_short(minX,maxX,target,function,**kwargs):
	
	#Base case
	if minX>=maxX:
		return minX

	#Midpoint evaluation
	middle = (minX+maxX)//2
	f = function(middle,**kwargs)

	#Binary step
	if f>=target:
		return binary_short(minX,middle-1,target,function,**kwargs)
	else:
		return binary_short(middle+1,maxX,target,function,**kwargs)

#################################################################################################
####Binary search that falls in the first occurrence of the target or its immediate successor####
#################################################################################################

def binary_long(minX,maxX,target,function,**kwargs):
	return 1+binary_short(minX,maxX,function,**kwargs)
