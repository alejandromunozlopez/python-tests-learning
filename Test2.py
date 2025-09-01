## Test 2 -----
## Libraries
import re
## VARIABLES
x = input('Please enter a number to be evaluated: ')
## Program
try:
    x1 = int(x)
except ValueError:
    print('Number given cannot be processed')
    exit()
##------------------------------------
##------------------------------------
##------------------------------------
y1 = int(2)
R = x1 % y1
if x1 != 4:
    print(f'Mod evaluation result is: {R}')
    if R == 0:
        print(f'Given number {x} is even')
    elif R == 1:
            print(f'Given number {x} is odd')
    else:
        print(f'Not evaluation in this condition for {x}')
else:
        print(f'Number {x} cant be evaluated... ')


                