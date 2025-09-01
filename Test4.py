## TEST 4 
        
#Imports
## VAR's
x  = int(input('Provide a number to be evaluated: '))
x1  = int(input('Provide a MIN EVAL RANGE: '))
x2 = int(input('Provide a MAX EVAL RANGE: '))
i = 1
list = []
#Program
for i in range(x1, x2):
    if x % i == 0:
        list.append(i)    
print(x)
print(list)
