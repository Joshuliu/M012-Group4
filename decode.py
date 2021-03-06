import ast
import os
import sys

try: # trying to load our binary code
	directory = os.path.dirname(os.path.abspath(__file__))
	binaryfile = open(directory + "/binary_code.json", "r") #reading the file
	# converting the string into dictionary
	contents = binaryfile.read()
	binary = ast.literal_eval(contents)
	#closing the file
	binaryfile.close()
except:  # if file is invalid/broken or missing
	print("binary_code.json invalid or missing. Is it in the same folder?")
	sys.exit() # exits file immediately if file invalid

# prompting the user to put in the file code is using
x = input('Enter file name to convert to text (should be in same folder as this script):')
# reading the file user put in
try:
	inputfile = open(directory + '/' + x, "r").read()
except:
	print("File invalid.")
	sys.exit() # exits file immediately if file invalid

inputfile = inputfile.split('.')[1] # retrieves binary part from "d.b" format

inputlist = [char for char in inputfile] # converts file input into big list
result = "" # stores result
num = 0 # stores which character to start with when iterating through long/short chars

while num < len(inputlist):

	code = "" # stores each long or short character
	if inputlist[num] == '0': #if short character
		code = inputlist[num] + inputlist[num+1] + inputlist[num+2] + inputlist[num+3]
		num += 4
	elif inputlist[num] == '1': #if long character 
		code = inputlist[num] + inputlist[num+1] + inputlist[num+2] + inputlist[num+3] + inputlist[num+4] + inputlist[num+5] + inputlist[num+6]
		num += 7
	else: # if unknown character...
		code = inputlist[num]
		num += 1

	try: 
		result += list(binary.keys())[list(binary.values()).index(code)] # finds char (or special chars) from binary value
	except: # if binary value does not exist or there is an invalid character...
		result += code # it will just be appended into final result.

print(result) # prints final result

binaryfile = open(directory + "/decode_output.txt", "w+").write(result) # saves to decode_output.txt
