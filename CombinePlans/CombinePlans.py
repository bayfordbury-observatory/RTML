#CombinePlans.py - Combine RTML files with different targets into one plan
#
# Example usage: 
# >>python CombinePlans.py Output.rtml StandardStar.rtml Target.rtml
#
# There is no maximum to the number of files that can be combined.
# Each file should only contain one plan and one target, otherwise only the first plan and target is used.
# Only the constraints from the first plan are used for the output
# Output file will be overwritten if it already exists

import sys

#Number of files to be combined
numFiles = len(sys.argv)-2

#Name of the output file
outputName = sys.argv[1]

print (numFiles, 'files to combine')

print ("Output > "+outputName)

if numFiles <2:
	raise Exception("At least two filenames must be provided")

#start with fresh file
with open(outputName, 'w'): pass
  
with open(outputName, 'w') as f:
   
	#first file
	filename = sys.argv[2]
	print("1 - Adding", filename)
	file = open(filename, 'r') 
	Lines = file.readlines() 
	
	#Loop through all lines until it reaches the end of the plan
	for line in Lines: 	
		if '</Target>' in line:
			#exit once we reach the end of the target
			f.write(line)
			break
		else:
			#otherwise write it to the output
			f.write(line)
			
	#Subsequent files
	
	for i in range(2, 1+numFiles):
		
		filename = sys.argv[i+1]
		print(i, "- Adding", filename)
		file = open(filename, 'r') 
		Lines = file.readlines() 

		foundPlan = False

		for line in Lines: 
		
			if '<Target ' in line:
				#Found the target tag
				f.write(line)
				foundPlan = True
			elif '</Target>' in line:
				#end of target, write and stop
				f.write(line)
				if i!=numFiles:
					break
			elif foundPlan:
				#otherwise write it to the output
				f.write(line)
