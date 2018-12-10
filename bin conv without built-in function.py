def convert(x):
    lst=[]
    y=x
    while y != 0:
        a=y%2
        lst.append(str(a))
        y=y//2
    lst.reverse()
    print('In binay =',"".join(lst))
    z=x
    lst2=[]
    while x != 0:
        a=x%8
        lst2.append(str(a))
        x=x//8
    lst2.reverse()
    print('In Octal =',"".join(lst2))
    lst3=[]
    while z != 0:
        remainder = changeDigit(z % 16)
        lst3.append(str(remainder))
        z = (z // 16)
    lst3.reverse()
    print('In hexadecimal =',"".join(lst3))

def changeDigit(digit):
    decimal =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for char in range(7):
        if digit == decimal[char - 1]:
            digit = hexadecimal[char - 1]
    return digit
    
    
