import numpy.linalg as lg
import numpy as np
import random


class Lattice:
	def __init__(self, time_size, space_size, dim, beta, linkType):
		self.sites = np.zeros(
			[time_size] + [space_size for _ in range(dim-1)],
			dtype=linkType
		)
		self.links = np.zeros(
			list(self.sites.shape) + [dim],
			dtype=linkType
		)
		self.dim = dim
		self.beta = beta
		self.linkType = linkType
		self.bases = np.array([
			np.array([1,0,0,0]),
			np.array([0,1,0,0]),
			np.array([0,0,1,0]),
			np.array([0,0,0,1]),
		])
		self.numSites = reduce(lambda a, b: a*b, self.links.shape)
		
		for link in self.iterLinks():
			self.links[link] = linkType.getRandomElement()


	def iterLinks(self):
		for site in self.iterSites():
			for mu in range(self.dim):
				yield tuple(list(site)+[mu])


	def iterSites(self):
		for i in range(self.numSites):
			indices = list()
			for dim in self.sites.shape:
				indices.append(i % dim)
				i = i / dim

			yield tuple(indices)


	def getNeighbors(self, site):
		shape = self.sites.shape
		neighbors = list()
		for i, dim in enumerate(shape):
			e = list(site)
			if site[i] > 0:
				e[i] = e[i]-1
			else:
				e[i] = dim-1
			neighbors.append(tuple(e))

			e = list(site)
			if site[i] < dim - 1:
				e[i] = e[i]+1
			else:
				e[i] = 0
			neighbors.append(tuple(e))

		return neighbors


	def getRandomSite(self):
		return tuple([random.randint(0, d-1) for d in self.sites.shape])


	def getRandomLink(self):
		return tuple([random.randint(0, d-1) for d in self.links.shape])


	def localAction(self, *links):
		S = 0.0
		for link in links:
			site1 = link[:-1]
			mu = link[-1]
			for nu in range(self.dim):
				if nu != mu:
					site2 = np.array(site1) - self.bases[nu]
					S += 5.0/3.0 * (
						self.plaquetteOperator(site1, mu, nu)
						+ self.plaquetteOperator(site2, mu, nu) 
					)

		return S


	def totalAction(self):
		S = 0.0
		for site in self.iterSites():
			for mu in range(self.dim):
				for nu in range(self.dim):
					if nu > mu:
						S += 5.0/3.0 * self.plaquetteOperator(site, mu, nu) 

		return S

	
	def plaquetteOperator(self, c, mu, nu):
		c = np.array(c)

		return 1.0/3.0 * np.trace(
			self.links[tuple(list(c%5)+[mu])]
			*self.links[tuple(list((c+self.bases[mu])%5)+[nu])]
			*self.links[tuple(list((c+self.bases[nu])%5)+[mu])].conjugate().T
			*self.links[tuple(list(c%5)+[nu])].conjugate().T
		).real

	
	def rectOperator(self, c, mu, nu):
		c = np.array(c)

		return 1.0/3.0 * np.trace(
			self.links[tuple(list(c%5)+[mu])]
			*self.links[tuple(list((c+self.bases[mu])%5)+[mu])]
			*self.links[tuple(list((c+2*self.bases[mu])%5)+[nu])]
			*self.links[tuple(list((c+self.bases[mu]+self.bases[nu])%5)+[mu])].conjugate().T
			*self.links[tuple(list((c+self.bases[nu])%5)+[mu])].conjugate().T
			*self.links[tuple(list(c%5)+[nu])].conjugate().T
		).real

	def metropolisUpdate(self):
		link = self.getRandomLink()
		U = self.linkType.getRandomElement()

		Si = self.localAction(link)
		self.links[link] = U * self.links[link]
		Sf = self.localAction(link)

		# print Sf - Si
		
		if np.random.rand() > min(1, np.exp(self.beta*(Sf-Si))):
			self.links[link] = U.conjugate().T * self.links[link]









