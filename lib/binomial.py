from __future__ import division
import numpy as np

class Binomial(object):

	def __init__(self,maxN=501,modulo=100003):
		self._maxN = maxN
		self._modulo = modulo
		self._binomial = np.ones((maxN,)*2,dtype=np.int)*-1

		#Initialize binomials with boundary conditions
		n,k = np.indices(self._binomial.shape)
		self._binomial[n==k] = 1
		self._binomial[n<k] = 0
		self._binomial[k==0] = 1

	#Compute binomial coefficients
	def binomial(self,n,k):

		if n<0:
			return 0
		
		if self._binomial[n,k]>-1:
			return self._binomial[n,k]

		for ni in range(1,n+1):
			for ki in range(1,k+1):
				self._binomial[ni,ki] = (self._binomial[ni-1,ki-1] + self._binomial[ni-1,ki])%self._modulo

		return self._binomial[n,k]

	#Query pre-computed binomial coefficients
	def binomial_query(self,n,k):
		binomial_coeff = self._binomial[n,k]
		binomial_coeff[n<0] = 0
		binomial_coeff[k<0] = 0
		return binomial_coeff