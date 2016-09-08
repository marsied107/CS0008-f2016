#Gets the amount of the purchase
purchase = float(input('Enter the amount of your purchase: '))

#calculates state sales tax
statetax = purchase * .05

#calculates county sales tax
countytax = purchase * .025

#calculates total sales tax
tax = statetax + countytax

#calculates the total sale
total = purchase + tax

#Displays all of the info
print('The amount of your purchase is $', format(purchase, ',.2f'))
print('The amount of the state tax is $', format(statetax, ',.2f'))
print('The amount of the county tax is$', format(countytax, ',.2f'))
print('The amount of total sales tax is $', format(tax, ',.2f'))
print('The total of your purchase is $', format(total, ',.2f'))