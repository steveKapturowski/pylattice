import os
from lattice import Lattice
from fields import SU3


def main():
	time_size = int(os.getenv("TIME_SIZE"))
	space_size = int(os.getenv("SPACE_SIZE"))
	dimension = int(os.getenv("DIMENSION"))
	beta = float(os.getenv("BETA"))

	lattice = Lattice(
		time_size, 
		space_size, 
		dimension, 
		beta,
		SU3,
	)
	
	print SU3.GELLMANN_MATRICES


if __name__ =="__main__":
	main()