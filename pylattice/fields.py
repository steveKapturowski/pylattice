import numpy as np


class SU3 (np.matrix):
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


	def __init__(self):
		pass


	def computeLocalAction(self):
		pass


	def getRandomElement(self):
		pass


	def getMeasure(self):
		pass

