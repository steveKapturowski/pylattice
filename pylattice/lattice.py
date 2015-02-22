import numpy as np
import random


class Lattice:
	def __init__(self, time_size, space_size, dim, beta, fieldType):
		print dim
		self.lattice = np.zeros(
			[time_size] + [space_size for _ in range(dim-1)],
			dtype=fieldType
		)
		print fieldType.GELLMANN_MATRICES
		self.beta = beta


	def getNeighbors(self, indices):
		shape = self.lattice.shape
		neighbors = list()
		for i, dim in enumerate(shape):
			e = list(indices)
			if indices[i] > 0:
				e[i] = e[i]-1
			else:
				e[i] = dim-1
			neighbors.append(tuple(e))

			e = list(indices)
			if indices[i] < dim - 1:
				e[i] = e[i]+1
			else:
				e[i] = 0
			neighbors.append(tuple(e))

		return neighbors



	def getRandomSite(self):
		return tuple([random.randint(0, d-1) for d in self.lattice.shape])








