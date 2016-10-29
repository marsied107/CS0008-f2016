#Ask the user to input the speed and how many hours they have traveled
speed = int(input('What is the speed of the vehicle in mph?: '))
hours = int(input('How many hours has it traveled?: '))

#Loop that calculates the distance traveled for each hour
for hour in range(hours):
    distance = 0
    print('Hour         Distance Traveled')
    print('______________________________')
    print((hour+1), ((hour+1)*speed))




