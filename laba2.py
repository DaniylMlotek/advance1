oper = input('enter an operation a/b:')
if oper == 'a':
    text = input('enter a text:')
    t = list(text)
    a = []
    for i in t:
        if i+ '-' +str(t.count(i)) not in a:
            a.append(i+ '-' +str(t.count(i)))
        print(a)
elif oper == 'b':
    text1 = input('enter a text:').split('1')  пофіксити спліт
    b = []
    for j in b:
        if len(j) >=3 and j not in b:
            b.append(j)
        print(b)