import random
print('Guess the number between 1-10... ')
num=random.randint(1,10)
guess=int(input('guess the number:'))
i=0
print('There will be only three chances')
while i<3:
    guess=int(input('guess again:'))
    i=i+1
    if guess==num:
        print('you won')
        break
else:
    print('you are out of chances')
    
