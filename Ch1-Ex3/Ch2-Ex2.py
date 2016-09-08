#Gets the projected sales
sales = float(input('What is the projected amount of total sales'))

#Assigns the percent value
percent = 0.23

#Calculates the total profit
profit = sales * percent

#Displays the profit
print('Your profit is $', format(profit, ',.2f'))
