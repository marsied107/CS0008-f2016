#
# MN: header with user, instructor and course info is missing
#
# Notes:
# MN: I would like you to insert more comments.
# MN: it does not run in python version 3.x
#

# opens and read the text file
filename = "f2016_cs8_a3.data.txt"
fh = open(filename, "r")
fh.close()

# MN: why not asking the user for the master list files?
dataSources= "f2016_cs8_a3.data.txt"
with open(dataSources) as fh:
    for line in fh:
        fh = open(dataSources, 'r')
        sourceFiles = fh.readlines()

# MN: why do you initialize this variable this way?
dataSources= "f2016_cs8_a3.data.txt"
fh = open(dataSources, "r")
sourceFiles = fh.readlines()
fh.close()

sourceFiles = [item.strip('\n') for item in sourceFiles]

# intialize data container
# intializes the variables
person_distances = {}
data = []
max = 0
maxkey = 0
min = -1
minkey = 0
# loop on all the data files
for source in sourceFiles:
    # open current data file for reading
    fh = open(source, "r")
    # loop on all lines
    for line in fh:
        # check if it is a header
        if not 'distance' in line:
            # read the whole file in
            # MN: here you read only the current line in
            data.append(line.strip('\n'))
            # MN: you need to perform the sum of all the lines 
            #     only when you have read the whole file in
            # MN: if you run this statement here, you will execute the sum
            #     everytime you read a new line in
            ## Creates the sum of all of the lines read
            #lines = sum(1 for lines in data)
            #
            line = line.strip('\n')
            # splits key and value
            (key, val) = line.split(',')
            #
            # MN: why dont you convert val right away so you do not have to convert it everytime 
            val = float(val)
            # Calculates total distances, max, and min
            if(key in person_distances):
                # person_distances[key].append(float(val))
                person_distances[key].append(val)
            else:
                #person_distances[key] = [float(val)]
                person_distances[key] = [val]
            
            # MN: this method will compute min or max on only the single distance
            #     not on the participant total distance
            if(val > max):
                max = val
                maxkey = key
            if(val < min or min == -1):
                min = val
                minkey = key

# MN: here is where you should compute the total number of lines
lines = sum(1 for lines in data)

# MN: are you computing the total distance?
distances = [item.strip('\n').split(',')[1] for item in data]

# Calculates the total distance
total_distance = sum(\
                    [float(item.strip('\n').split(',')[1])\
                     for item in data])

# Calculates how many people have multiple records
multi_record_count = 0
for key in person_distances:
    if(len(person_distances[key])>1):
        multi_record_count +=1

# Creates an output file of Peoples names, how many times they ran,
# and each of their distances
# MN: why do you recont multiple records, you already did it in the previous code block 
multi_record_count = 0
total_participants = 0
f=open('f2016_cs8_a3.output.csv', 'w')
for key in person_distances:
    # MN: why do you insert only the participants with multiple records in the output file?
    if(len(person_distances[key])>1):
        multi_record_count += 1
        f.write(key)
        f.write(',')
        f.write(str(len(person_distances[key])))
        f.write(',')
        f.write(str(sum(person_distances[key])))
        f.write('\n')
        total_participants += 1
f.close()

# Calculates how many files the file reads
# MN: why do you read again the master list file?
#     you already that information in "sources"
#     I would have done as follow:
#     num_lines = len(sources)
num_lines = sum(1 for line in open('f2016_cs8_a3.data.txt'))


# Prints all of the data
print('Number of Input files read  :     ',(num_lines))
print('Total number of lines read  :     ',(lines))
print('Total distance run          :     ',(total_distance))
print('Max distance run            :     ',(max))
print('by participant              :     ',maxkey)
print('Min distance run            :     ',min)
print('by participant              :     ',minkey)
print('Total number of participants:     ',len(person_distances.keys()))
print('  Number of participants            ')
print('with multiple records       :     ',(multi_record_count))

