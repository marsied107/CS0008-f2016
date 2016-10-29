time = int(input('Enter the amount of time you have ran on the treadmill: '))

calories = 0
for i in range(time):
    calories += 3.4

print('You burned this many calories: ',format(calories, ',.2f'))