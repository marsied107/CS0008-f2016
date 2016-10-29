#Prompts the user to enter whether they are using Metric or USC system
system = int(input('If you are using the metric system enter 1 if you are using the USC system enter 2: '))

#Prompts the user to enter how far they have driven and how much gas they have used
distance = float(input('Enter how far you have driven in miles or kilometers: '))
gasoline = float(input('Enter how much gas you have used in gallons or liters: '))

#Converts the quantities entered by the user into the other system
if system == 1:
    liters = gasoline
    kilometers = distance
    miles = distance * 0.62137
    gallons = gasoline * 0.264172
else:
    miles = distance
    gallons = gasoline
    liters = gasoline * 3.78541
    kilometers = distance * 1.60934

#computes the fuel consumption
miles_g = miles/gallons
liters_k = 100*liters/kilometers

#Computes the fuel consuption rating
if liters_k > 20:
    rating = ('Extremely Poor')
else:
    if liters_k == 20 >= liters_k > 15:
        rating = ('Poor')
    else:
        if liters_k == 15 >= liters_k > 10:
            rating = ('Average')
        else:
            if liters_k == 10 >= liters_k > 8:
                rating = ('Good')
            else:
                if liters_k <= 8:
                    rating = ('Excellent')

print('                             USC             Metric')
print('Distance_________:  ', format(miles, ',.3f'),('miles'), format(kilometers, ',.3f'),('Km'))
print('Gas______________:  ', format(gallons, ',.3f'),('gallons'), format(liters, ',.3f'),('Liters'))
print('Consumption______:  ', format(miles_g, ',.3f'),('mpg'), format(liters_k, ',.3f'),('1/100Km'))
print('Gas Consumption Rating:', (rating))
