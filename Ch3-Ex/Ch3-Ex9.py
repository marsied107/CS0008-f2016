#Asks the user for a number between 0 and 36
number = (input('Enter a number 0-36: '))

#Makes sure the number is an integer
number = int(number)

#tests if number is between 0 and 36
if number < 0 or number > 36:
    print ('Give me a number between 0 and 36')

if number == 0:
    color = "green"
elif (number >= 1 and number <= 10) \
        or \
     (number >= 19 and number <= 28):
    if number %2 == 0:
        color = 'black'
    else:
        color = 'red'
elif (number >= 11 and number <= 18) \
        or \
     (number >= 29 and number <= 36):
    if number %2 == 0:
        color = 'red'
    else:
        color = 'black'

print('Your color is', (color))