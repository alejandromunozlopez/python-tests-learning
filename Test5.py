
# TEST 5
import random

l1 =[]
l2 =[]
x = []
r1 = random.randint(0,30)
r2 = random.randint(0,30)
for i in range(1,r1+1):
    x1 = random.randint(0,100)
    l1.append(x1)
for i in range(1,r2+1):
    x2 = random.randint(0,100)
    l2.append(x2)
print(f'{l1}\n{l2}')

for l1 in l1:
    if l1 in l2:
        if l1 not in x:
            x.append(l1)

print(x)
print(f'Times of merged values...{len(x)}')
