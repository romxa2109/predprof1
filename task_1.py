File = open('students.csv',encoding = "UTF-8")
St = []
for i in File:
    St.append(i.split(','))

for i in St:
    if 'Хадаров Владимир' in i[1]:
        print('Ты получил: ', i[4][:-1],', за проект - ', i[2], sep='')
        break


for i in range(1, len(St)-1):
    for j in range(len(St)-2, i-1, -1):
        if St[j][3] < St[j+1][3]:
            St[j],St[j+1] = St[j+1],St[j]

Sred = []
Summ = int(St[1][4])
k = 1
for i in range(2, len(St)):
    if St[i][3] == St[i-1][3]:
        if not('None' in St[i][4]):
            k+=1
            Summ+=int(St[i][4])
    else:
        Sred.append([St[i-1][3], str(round(Summ/k, 3))+'\n'])
        if not('None' in St[i][4]):
            k = 1
            Summ = int(St[i][4])
        else:
            k = 0
            Summ = 0

for i in range(1, len(St)):
    if 'None' in St[i][4]:
        for j in Sred:
            if St[i][3] == j[0]:
                St[i][4]= j[1]
                break

File1 = open('students_new.csv', 'w', encoding = "UTF-8")
for i in range(0, len(St)):
    File1.write(str(St[i][0])+','+str(St[i][1])+','+str(St[i][2])+','+str(St[i][3])+','+str(St[i][4]))

File.close()
File1.close()
    
