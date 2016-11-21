#opens and read the text file
filename = "f2016_cs8_a3.data.txt"
fh = open(filename, "r")
fh.close()

dataSources= "f2016_cs8_a3.data.txt"
with open(dataSources) as fh:
    for line in fh:
        fh = open(dataSources, 'r')
        sourceFiles = fh.readlines()

dataSources= "f2016_cs8_a3.data.txt"
fh = open(dataSources, "r")
sourceFiles = fh.readlines()
fh.close()

sourceFiles = [item.strip('\n') for item in sourceFiles]

#intialize data container
#intializes the variables
person_distances = {}
data = []
max = 0
maxkey = 0
min = -1
minkey = 0
#loop on all the data files
for source in sourceFiles:
    #open current data file for reading
    fh = open(source, "r")
    #loop on all lines
    for line in fh:
        #check if it is a header
        if not 'distance' in line:
            #read the whole file in
            data.append(line.strip('\n'))
            #Creates the sum of all of the lines read
            lines = sum(1 for lines in data)
            line = line.strip('\n')
            #splits key and value
            (key, val) = line.split(',')
            #Calculates total distances, max, and min
            if(key in person_distances):
                person_distances[key].append(float(val))
            else:
                person_distances[key] = [float(val)]
            if(val > max):
                max = val
                maxkey = key
            if(val < min or min == -1):
                min = val
                minkey = key


distances = [item.strip('\n').split(',')[1] for item in data]
#Calculates the total distance
total_distance = sum(\
                    [float(item.strip('\n').split(',')[1])\
                     for item in data])
#Calculates how many people have multiple records
multi_record_count = 0
for key in person_distances:
    if(len(person_distances[key])>1):
        multi_record_count +=1
#Creates an output file of Peoples names, how many times they ran,
#and each of their distances
multi_record_count = 0
total_participants = 0
f=open('f2016_cs8_a3.output.csv', 'w')
for key in person_distances:
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
#Calculates how many files the file reads
num_lines = sum(1 for line in open('f2016_cs8_a3.data.txt'))
#Prints all of the data
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
