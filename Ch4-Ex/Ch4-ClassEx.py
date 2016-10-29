day = 5
rt = 0

while day == 5:
    x = int(input('amount of bugs?:' ))
    if x <= 0:
        x = int(input('Input a different number:' ))

    while x < 0:
        x = int(input('jerk # days > 0'))

rt = rt + x
day = day - 1

print('Total bugs is :', (rt))