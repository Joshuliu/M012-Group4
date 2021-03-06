import ast # lib to interpret string into dict
import os # lib to find path of files
import sys # lib to exit file


try: # trying to load our binary code
    directory = os.path.dirname(os.path.abspath(__file__))
    binaryfile = open(directory + "/binary_code.json", "r") #reading the file
    # converting the string into dictionary
    contents = binaryfile.read()
    binary = ast.literal_eval(contents)
    #closing the file
    binaryfile.close()
except: # if file is invalid/broken or missing
    print("binary_code.json invalid or missing. Is it in the same folder?")
    sys.exit() # exits file immediately if file invalid

# prompts user for file that they want to input
x = input('Enter file name to convert to binary (should be in same folder as this script): ')

try:
    inputfile = open(directory + '/' + x, "r").read() # opens and reads the file that user inputed
except:
    print("File invalid.")
    sys.exit() # exits file immediately if file invalid

inputlist = [char for char in inputfile] # converts all chars in the inputfile into a list
result = "" # stores result
num = 0 # stores which character to iterate through 

while num < len(inputlist): # ensures char being iterated is in inputlist

    count = -1 # stores length of each test to find largest number of chars in our binary code
    finalcount = -1 # stores length of final largest number of chars in our binary code
    test = "" # stores each test to find largest number of chars in our binary code
    final = "" # stores final largest number of chars in our binary code 
    for x in range(5): # testing next if char, next 2 chars,... next 5 chars in our binary code
        if num+x < len(inputlist): # if there are any chars left to test
            count += 1 # indicates what index of list has been iterated over
            if test + inputlist[num + x] in binary.keys(): # if next x characters are in our binary code
                final = test + inputlist[num + x] # updates string to hold largest special characters (could just be one character)
                finalcount = count # updates finalcount to determine which character to iterate over next

            test += inputlist[num + x] # updates the next biggest group of chars to test
        else: # stop iterating over list if no more chars to test
            break

    if final != '': 
        num += 1 + finalcount # determines next character to iterate over
        result += binary[final] # adds most updated binary numbers to the final result
    else: # if character is not in our binary code...
        num += 1 # we skip the character

db = str(len(result)) + "." + result

print(db) # prints "d.b" format of final characters

binaryfile = open(directory + "/encode_output.txt", "w+").write(db) # saves to encode_output.txt
