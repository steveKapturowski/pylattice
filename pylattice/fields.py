import numpy as np
from scipy import linalg


class SU3(np.matrix):
	GELLMANN_MATRICES = np.array([
		np.matrix([ #lambda_1
			[0, 1, 0],
			[1, 0, 0],
			[0, 0, 0],
		], dtype=np.complex),
		np.matrix([ #lambda_2
			[0,-1j,0],
			[1j,0, 0],
			[0, 0, 0],
		], dtype=np.complex),
		np.matrix([ #lambda_3
			[1, 0, 0],
			[0,-1, 0],
			[0, 0, 0],
		], dtype=np.complex),
		np.matrix([ #lambda_4
			[0, 0, 1],
			[0, 0, 0],
			[1, 0, 0],
		], dtype=np.complex),
		np.matrix([ #lambda_5
			[0, 0,-1j],
			[0, 0, 0 ],
			[1j,0, 0 ],
		], dtype=np.complex),
		np.matrix([ #lambda_6
			[0, 0, 0],
			[0, 0, 1],
			[0, 1, 0],
		], dtype=np.complex),
		np.matrix([ #lambda_7
			[0, 0,  0 ],
			[0, 0, -1j],
			[0, 1j, 0 ],
		], dtype=np.complex),
		np.matrix([ #lambda_8
			[1, 0, 0],
			[0, 1, 0],
			[0, 0,-2],
		], dtype=np.complex) / np.sqrt(3),
	])


	def computeLocalAction(self):
		pass


	#TODO: cache group elements and do random lookup to boost performance
	@classmethod
	def getRandomElement(self):
		#exp(alpha_i * A_i) should be randomly distributed 
		#over SU(3) for random alpha_i, A_i generators of SU(3)
		return linalg.expm2(1j*self.GELLMANN_MATRICES.T.dot(np.random.rand(8)))


	@classmethod
	def getMeasure(self):
		pass




