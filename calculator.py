
#Calculator Project


a=float(input('enter value a:'))
b=float(input('enter value b:'))
op=input('enter the operators (+,-,/,*,%,**)' + '' )


if op=='+':
    print(a+b)

elif op=='-':
    print(a-b)

elif op=='/':
    print(a/b)

elif op=='*':
    print(a*b)

else:
   print('invalid value')

