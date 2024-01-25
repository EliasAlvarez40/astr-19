#create the class of my favorite animal
class Frog:

	#defining all useful information
	name = "Desert Rain Frog"
	L_arms = 0.01	#length of arms is 1cm
	L_legs = 0.01 	#length of legs is 1cm
	N_eyes = 2 		#number of eyes
	tail = False	#does not have a tail
	furry = False 	#Does not have fur

	#initialization function that sets the values of the data members
	def __init__(self,name,L_arms,L_legs,N_eyes,tail,furry):
		self.name = name
		self.L_arms = L_arms
		self.L_legs = L_legs
		self.N_eyes = N_eyes
		self.tail = tail
		self.furry = furry



def main():	
	#declare a dictionary for 
	Desert_Rain_Frog = Frog("Desert Rain Frog",0.01,0.01,2,False,False)

	print(f"My favorite animal is the {Desert_Rain_Frog.name}.")
	print(f"Arm length in {Desert_Rain_Frog.L_arms} meters.")
	print(f"Leg length in {Desert_Rain_Frog.L_legs} meters.")
	print(f"They have {Desert_Rain_Frog.N_eyes} eyes.")
	print(f"Does {Desert_Rain_Frog.name} have a tail? {Desert_Rain_Frog.tail}.")
	print(f"Does {Desert_Rain_Frog.name} have fur? {Desert_Rain_Frog.furry}.")


#if the main() function exists run it
if __name__ == "__main__":
	main()