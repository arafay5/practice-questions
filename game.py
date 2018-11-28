import random
x=random.randint(1,100)
lst=[]
y=int(input('Guess the number between 1 to 100:'))
while x != y:
    if x>y:
        y=int(input('Too low! Try again: '))
    else:
        y=int(input('Too High! Try again: '))
    lst.append(y)
print('Congratulation! You have got it in just '+str(len(lst))+' guesses.')
        
