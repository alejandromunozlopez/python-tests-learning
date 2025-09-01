## TEST 1 --- Name and Age as inputs, giving a result of the year this person is turning 100 + Insights

## Libraries used in example
## -----
from datetime import datetime 

## VAR Definition
## -----
name = input('Provide your name: ').capitalize()
age = int(input('Whats your age: '))

## BODY & CACULATIONS
## -----
if age > 0:
    today = datetime.now()
    today_year = datetime.strftime(today, '%Y')
    today_year_int = int(today_year)
    y = 100 - age
    today_year_int += y
    print(f'Hello {name}, Year turning 100 will be: {today_year_int}')
    copies =  int(input('How many times you want this message to be displayed?: ')) 
    m1 = str(f'Hello {name}, Year turning 100 will be: {today_year_int}\n')
    print( copies * m1)
else:   
    print(f'{name}... Thats not a proper age')






