import math
operation = input('''
*
/
+
-
select your operation:
''')

x = int(input('enter your first number:'))
y = int(input('enter your second number:'))


if operation == '*':
    print('your result',x*y)
elif operation == '/':
    print('your result',x/y)
elif operation == '+':
    print('your result',x+y)
elif operation == '-':
        print('your result',x-y)
else:
    print('incorrect operation,have a nice day')

