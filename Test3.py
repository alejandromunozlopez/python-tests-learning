
## TEST 3 -----------
        
## Import
import random
#Define Vars
T = 0
F = 0
compare = int(input('Comparision value: '))

y = []
x = random.sample(range(0,1000),10)

## Problem
print(f'List to be evaluated is: {x}')
for x in x:
    if x < compare:
        print(f'Value {x} is less than compared value {compare}')
        y.append(x)
        T += 1
    else:
        print(f'Value {x} not less than {compare}')
        F += 1 
print(f'{y}, amount of less values vs compared is {len(y)}')
print(f' Times True condition {T}')
print(f' Times False condition {F}')
