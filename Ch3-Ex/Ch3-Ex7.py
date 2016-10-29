#sets the colors equal to false
red = False
blue = False
yellow = False


#Prompts the user to enter one of the primary colors
color1 = bool(input('Enter one of the primary colors either red, blue, or yellow: '))
color2 = bool(input('Enter another one of the primary colors either red, blue, or yellow not one you entered before'))

#tells you what colors mix together to create another color
if color1 or color2 == red and color2 or color1 == blue:
    print('Mixing these two colors gives you purple')

else:
    if color1 or color2 == red and color2 or color1 == yellow:
        print('Mixing these two colors gives you orange')

    else:
        if color1 or color2 == blue and color2 or color1 == yellow:
            print('Mixing these two colors gives you green')

        else:
            if color1 or color2 != blue or red or yellow:
                print('Enter red, blue, or yellow')