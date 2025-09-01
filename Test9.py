
## TEST 9 ------------------------------------

##Import
import random

#VARs
target = random.randint(1,9)
times = 1

#Solution
print('Hello! "Guess the Number -> game"                 \
      \nThe number to guess is between 1 and 9            \
       \nType Exit if you want to end this game '  ) 

print()
while True:
    value = input('Enter a number now!: ')

    if isinstance(value,str):
        try:
            value = int(value)
            while True:
                if value > target:
                    times += 1
                    print('Your attempt is above the mystery number... ')
                elif value < target:
                    times += 1
                    print('Your attempt is below the mystery number... ')
                elif value == target:
                    print(f'Congratulations! Your value is the same as the mystery one! \
                        \n Total attempts: {times} ')    
                    break
                value = int(input('Enter a number now!: '))
            print()
            break
        except  ValueError :
            pass
        
        if value.capitalize() != 'Exit':
            print('Data not valid... ')
        elif value.capitalize() == 'Exit':
            break

  
        
        
        