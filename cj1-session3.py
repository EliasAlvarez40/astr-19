#Defining the function f(x)
def Cube(x):
	return (x ** 3.0) + 8.0	#f(x) is equal to (x^3 + 8)

def main():

	x = 9.0		#defining the value x is equal too
	print(Cube(x)) #printing function

	#if the function is greater than 27 say "YAY!"
	if Cube(x) > 27:
		print("YAY!")
	else: 
		print("NO!")

if __name__=="__main__":
	main() 

