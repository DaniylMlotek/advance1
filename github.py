while True:
    alf_eng = 'absdefghijklmnopqrstuvwxyzabsdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVW'
    alf_ua = 'aбвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяабвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    step = int(input('enter a key:'))
    lang = input('enter a language eng/ua:')
    message = input('message deshif:')
    result = ''
    if lang == 'eng':
        for i in message:
            cell = alf_eng.find(i)
            new_cell = cell + step
            if i in alf_eng:
                result += alf_eng[new_cell]
            else:
                result +=i
    else:
        for i in message:
            cell = alf_ua.find(i)
            new_cell = cell + step
            if i in alf_ua:
                result +=alf_ua[new_cell]
            else:
                result +=i
    print(result)
