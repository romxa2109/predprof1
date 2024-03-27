File = open('students.csv',encoding = "UTF-8")
St = []
for i in File:
    St.append(i.split(','))


for i in range(2, len(St)):
        temp = St[i]
        j = i - 1
        while (j >= 0 and temp[4] > St[j][4]):
            St[j + 1] = St[j]
            j = j - 1
        St[j + 1] = temp

print('10 класс:')
i = 0
for j in range(1, 4):
    while i<len(St):
        i+=1
        if '10' in St[i][3]:
            buf = St[i][1].split()
            print(j, 'место:', buf[1][0]+'. '+buf[0])
            i+=1
            break

File.close()

    
