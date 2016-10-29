def main():
    budget = float(input('Enter the amount you have budgeted for a month: '))

    cont = 'y'

    while cont == 'y':
        expense = float(input('Enter an expense: '))

        budget = budget - expense

        print('This is the money you have left: ', (budget))

        cont = raw_input('Do you want to calculate another expense?(enter y for yes, e to exit):' )
main()



