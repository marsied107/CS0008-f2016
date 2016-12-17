#user: Marielle Davis
#Instructor: Max Novelli
#Course: Int Programming 1
#Final Project
#12-16-16

#starts class
class participant:

    #name of participant
    name = "unknown"
    #total distance run
    distance = 0
    #total number of runs
    runs = 0

    #initializer methods
    def __init__(self, name, distance=0):
        #set name
        self.name = name
        #set distance if not zero
        if distance > 0:
            #set distance
            self.distance = distance
            #set number of runs
            self.runs = 1
            #end if


    #addDistance class
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
            #end if


    #addDistances class
    def addDistances(self, distances):
        #loops the list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
                #end if
                #end for

    #returns the name
    def getName(self):
        return self.name

    #returns total distance
    def getDistance(self):
        return self.distance

    #returns number of runs
    def getRuns(self):
        return self.runs

    #turns object into a string
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')

    #converts to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])

def getDataFromFile(file):
    #initializes list
    output = []
    #reads file by line
    for line in open(file,'r'):
        #excludes the header
        if "distance" in line:
            #skips line
            continue
        #removes \n and split line at ","
        temp1 = line.rstrip('\n').split(',')
        try:
            #append to dictionary
            #remove unwanted spaces and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            #skips incorrectly formatted lines
            print('Invalid row : '+line.rstrip('\n'))
    #end for
    #return
    return output

#ask for master file
masterFile = input("Please provide master file : ")

#read master file and extract data files
try:
    dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
except:
    print("Impossible to read master file or invalid file name")
    exit(1)

#sum of all the lists
rawData = sum([getDataFromFile(file) for file in dataFiles],[])

#sum of all the elements in the files
numberFiles = len(dataFiles)

#sum of the second item in raw data
totalLines = len(rawData)

#sum of distance
totalDistanceRun = sum([item['distance'] for item in rawData])

#initializes dictionary
participants = {}

#loops records
for item in rawData:
    #check if the names have been found
    #if it is new initialize elements
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    #insert distance in the list
    participants[item['name']].addDistance(item['distance'])

minDistance = { 'name' : None, 'distance': None }
#max distance run
maxDistance = { 'name' : None, 'distance': None }
#initializes dictionaey
apparences = {}

#finds the total distance run for each person
for name, object in participants.items():
    #gets total distance run by one person
    distance = object.getDistance()
    #check to update min
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    #check to update max
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance

    #gets number of runs
    participantAppearences = object.getRuns()

    #check if we need to initialize
    if not participantAppearences in apparences.keys():
        apparences[participantAppearences] = []
    apparences[participantAppearences].append(name)

#finds total number of participants
totalNumberOfParticipant = len(participants);

#find total number of people with more than one record
#extracts all the people that have multiple runs
totalNumberOfParticipantWithMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])

#set format strings
integer = '5d'
flt = '12.5f'
string = '20s'

#provide requested output
print("")
print(" Number of Input files read   : " + format(numberFiles,integer))
print(" Total number of lines read   : " + format(totalLines,integer))
print("")
print(" Total distance run           : " + format(totalDistanceRun,flt))
print("")
print(" Max distance run             : " + format(maxDistance['distance'],flt))
print("   by participant             : " + format(maxDistance['name'],string))
print("")
print(" Min distance run             : " + format(minDistance['distance'],flt))
print("   by participant             : " + format(minDistance['name'],string))
print("")
print(" Total number of participants : " + format(totalNumberOfParticipant,integer))
print(" Number of participants")
print("  with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords,flt))
print("")

#creates output file
outputFile = "f2016_cs8_man8_a3.output.csv"
#opens file
fh = open(outputFile,'w')
#writes header in file
fh.write('name,records,distance\n')
#loop on all the participants
for name, object in participants.items():
    #write line in file
    fh.write(object.tocsv() + '\n')
#close files
fh.close()