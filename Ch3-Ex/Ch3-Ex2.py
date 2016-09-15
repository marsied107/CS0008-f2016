#Asks for the length and width of the two rectangles
length1 = float(input('Enter the length of rectangle 1: '))
width1 = float(input('Enter the width of rectangle 1: '))
length2 = float(input('Enter the length of rectangle 2: '))
width2 = float(input('Enter the width of rectangle 2: '))

#Calculates the area of rectangle 1
area1 = length1 * width1

#Calculates the area of rectangle 2
area2 = length2 * width2

#Tells you what rectangle has the greatest area
if area1 > area2:
    print('The area of rectangle 1 is greater than rectangle 2')
else:
    if area2 > area1:
        print('The area of rectangle 2 is greater than rectangle 1')
    else:
        if area1 == area2:
            print('The area of rectangle 1 and 2 are the same')