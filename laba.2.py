oper = input('enter an action a/b:')
if oper == 'a':
    text = input('enter a text:').split()
    a = ''
    for i in sorted(text):
        a = a+ "," +i
    print(a)
if oper == 'b':
    text1 = input('enter a text:')
    d = {}
    for i in set(text1):
        d[i] = text1.count(i)
    print(d)
