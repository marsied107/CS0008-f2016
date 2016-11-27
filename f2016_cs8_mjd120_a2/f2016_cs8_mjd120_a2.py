#
# MN: header with user, instructor and course info is missing
#
# MN: there is not enough comments on each block of code
#

# Creates a loop to read each line of the data file
# Converts the string into an array
# Adds one for each line and adds the data together
# Removes the last line
# Returns the total number of lines and total amount of data
def processFile(fh):
    partial_distance = 0
    line_number = 0
    for line in fh:
        line_number += 1
        line = line.rstrip("\n")
        temp = line.split(",")
        dist = float(temp[1])
        partial_distance += dist
    return line_number,partial_distance

# Prints out the info that is returned from the function
# Formats the key at n-length characters
# Formats the the string so that it is 20 spaces long
# Formats the integer so that it is 10 spaces long
# Formats the float so that it is 10 spaces and 3 decimal spaces long
def printKV(key, value, klen = 0):
    if isinstance(value, str):
        print key + " " + format(value, '20,.f')
    elif isinstance(value, int):
        print key + " " + format(value, '10,')
    elif isinstance(value, float):
        print key + " " + format(value, '10,.3f')

# Sets total distance and total number = to 0
# Creates the loop to open the function, return, and quit
# Initalizes the printKV function
total_distance = 0
total_number = 0
name = input('File to be read: ')
while name and name != "quit" and name != "Q":
    fh = open(name, 'r')
    partial_total_number, partial_distance = processFile(fh)

    printKV('Partial Total # of Lines: ', partial_total_number)
    printKV('Partial distance run: ', partial_distance)
    fh.close
    total_distance += partial_distance
    total_number += partial_total_number
    name = input('File to be read: ')

printKV('Total # of lines: ', total_number)
printKV('Total Distance: ', total_distance)
