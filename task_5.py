import random

def Hash(name):
    Alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    s = name
    p = 67
    m = 10**9 + 9
    h = 0
    for i in range(len(name)):
        h += (Alf.find(s[i])+1)*(p**i)
    h = h%m
    return str(h)

File = open('students.csv',encoding = "UTF-8")
St = []
for i in File:
    St.append(i.split(','))


for i in range(1, len(St)):
    St[i][0] = Hash(St[i][1])


File1 = open('students_with_hash.csv', 'w', encoding = "UTF-8")
for i in range(0, len(St)):
    File1.write(str(St[i][0])+','+str(St[i][1])+','+str(St[i][2])+','+str(St[i][3])+','+str(St[i][4]))

File.close()
File1.close()
    
                
                
