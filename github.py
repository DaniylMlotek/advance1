while True:
    alf_ua = 'aбвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяабвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯabsdefghijklmnopqrstuvwxyzabsdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVW1234567890'
    step = 1
    message = input('message deshif:')
    result = ''
    for i in message:
        cell = alf_ua.find(i)
        new_cell = cell + step
        if i in alf_ua:
            result += alf_ua[new_cell]
        else:

            result += i
    print(result)
