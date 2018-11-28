x=input('enter any number : ')
y=list(x)
sum=0
for char in y:
    print(char)
    sum= sum + (int(char)**3)
    print(sum)
if sum==int(x) :
    print('the number is armstrong')
else:
    print('the number is not armstrong')
 
