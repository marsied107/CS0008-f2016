#Prompts the user to enter their age
age = int(input('Enter your age as a number: '))



if (age <= 1):
    print('You are classified as an infant')
else:
    if age == 1 < age < 13:
        print('You are classified as a child')
    else:
        if age == 13 <= age < 20:
            print('You are classified as a teenager')
        else:
            if age >= 20:
                print('You are classified as an adult')