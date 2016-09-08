#Gets prices of 5 items
item1 = float(input('Enter the price of item 1: '))
item2 = float(input('Enter the price of item 2: '))
item3 = float(input('Enter the price of item 3: '))
item4 = float(input('Enter the price of item 4: '))
item5 = float(input('Enter the price of item 5: '))

#Calculates the subtotal
subtotal = item1 + item2 +item3 + item4 + item5

#Calculates the sales tax
tax = subtotal * 0.07

#Calculates the total
total = tax + subtotal

#Displays the subtotal, tax, and total
print('Your subtotal is $', format(subtotal, ',.2f'))
print('Your tax is $', format(tax, ',.2f'))
print('Your total is $', format(total, ',.2f'))