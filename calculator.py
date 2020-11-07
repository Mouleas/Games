import math



#getting input
a=float(input('Enter the number:'))
b=float(input('Enter the number:'))
c=input('Enter the arithmetic operation:')


#operations
addition=a+b
subtract=a-b
multiplication=a*b
division=a/b
modulus=a%b

#conditions
if c=='+':
    print('The sum of the given two number is ',addition)

elif c=='-':
    print('The subration the given two number is ',subtract)

elif c=='*':
    print('The multiplication of the given two number is ',multiplication)

elif c=='/':
    print('The division the given two number is ',division)

elif c=='%':
    print('The modulus of the given two number is ',modulus)

else:
    print('operation is invalid...')

