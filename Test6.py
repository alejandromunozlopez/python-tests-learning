
## Test6
    ## Evaluate a input if is a palindrome
    
evaluation = input('Write a word to evaluate if palyndrome: ')
letters_T = len(evaluation)    
concate = str()
print(f'Given word is:{evaluation}')


for i in evaluation:
    letter_last = evaluation[letters_T-1:letters_T]
    concate += letter_last
    letters_T -= 1

if concate == evaluation:
    print(f'Given word is a palindrome!! \n {concate} \n {evaluation}')
else:
    print(f'Given word is not a palindrome....\n {concate} \n {evaluation}')