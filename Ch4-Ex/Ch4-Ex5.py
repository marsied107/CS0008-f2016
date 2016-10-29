#Asks for the the number of years you want to enter
total_years = int(input('Enter the number of years: '))

#Loop that displays what year you are inputing
for years in range(total_years):
    total = 0
    print('Year', (years+1))
    print('________________')
    #Has you input the inches of rainfall for each month
    print('Enter the inches of rainfall for each month')
    all_months = ('January ', 'February ', 'March ', 'April ', 'May ', 'June ', 'July ', 'August ', 'September ', 'October ', 'November ',
    'December ')
    for month in all_months:
        inches = float(input(month))
        total += inches
#Gives the total inches of rainfall
total_inches = total
#Gives the total number of months
total_month = total_years * 12
#Gives the average amount of rainfall per month
average_inches = total / total_month
#Prints the calculated information
print('The total number of months is: ',(total_month))
print('The total inches of rainfall is: ',(total_inches))
print('The average amount of rainfall per month is: ',(average_inches))
