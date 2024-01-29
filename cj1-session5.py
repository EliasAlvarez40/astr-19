import numpy as np  
from astropy.table import Table

def main():
	#np.linspace
	#np.arange
	x = np.linspace(0,2.0*np.pi,1000)
	y = np.sin(x)
	z = x**2

	data_table = Table()
	data_table["x"] = x
	data_table["x"] = y
	data_table["z"] = z
	print(data_table)

	#some_array = np.arange(0,100,2)
	#print(some_array)


if __name__ == "__main__":
	main()