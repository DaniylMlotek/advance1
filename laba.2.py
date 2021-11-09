oper = input('enter ur operation a/b:')
if oper == 'a':
    o = []
    text = input('enter ur text: ')
    for i in range(len(text)):
        if text[i] not in o and text[i] not in " ,.": 
            o.append(text[i])  
            o.append(text.count(text[i])) 
    print(o)

elif oper == 'b':
    text1 = input('enter ur text: ').split(' ')
    p = []
    for j in text1:
        if len(j) >= 3 and str.lower(j) not in p:
            p.append(str.lower(j))
    print(sorted(p))
