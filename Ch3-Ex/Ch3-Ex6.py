#Prompts the user to enter the month,day, and year
month = int(input('Enter a month in a numeric form: '))
day = int(input('Enter a day of the month in numeric form: '))
year = int(input('Enter the last two digits of the year: '))

if year == month * day:
    print('This is a magic date!')
else:
    print('This date is not magic')
