#Prompts the user to enter the mass of the object
mass = float(input('Enter the weight of your object: '))

#caluclates the objects
weight = mass * 9.8

#tests if the number is between 100 and 500
if weight < 100:
    print('Your object is too light')
if weight > 500:
    print('Your object is too heavy')

print('Your objects weighs', format(weight, ',.2f'))
