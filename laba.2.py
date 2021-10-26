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
# # t = list(tet)  -строку переводить в масив або кожну букву робить елементом масиву
# a = [] створює пустий масив
# t.count(i) кількість символів і по строці t
# a.append(i + '-' + str(t.count(i))) -добавляє елемент в мaсив