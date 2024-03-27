File = open('students.csv',encoding = "UTF-8")
St = []
for i in File:
    St.append(i.split(','))

while True:
    flag = False
    zapros = input('Введите запрос - ')
    if zapros == 'СТОП':
        break
    else:
        for i in range(len(St)):
            if St[i][2] == zapros:
                buf = St[i][1].split()
                print('Проект №', St[i][2], 'делал:', buf[1][0]+'. '+buf[0], 'он(а) получил(а) оценку - ', St[i][4][:-1])
                flag = True
        if not(flag):
            print('Ничего не найдено.')

File.close()
                
                
