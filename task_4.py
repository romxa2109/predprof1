import random

def Genlogin(name):
    login = ''
    buf = name.split()
    login = buf[0]+'_'+buf[1][0]+buf[2][0]
    return login


def Genpass(n):
    Alf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    pas = ''
    for i in range(n):
        pas+=Alf[random.randint(0, len(Alf)-1)]
    return pas

File = open('students.csv',encoding = "UTF-8")
St = []
for i in File:
    St.append(i.split(','))

St[0][4] = St[0][4][:-1]
St[0].append('login')
St[0].append('password'+'\n')
for i in range(1, len(St)):
    St[i][4] = St[i][4][:-1]
    St[i].append(Genlogin(St[i][1]))
    St[i].append(Genpass(8)+'\n')

File1 = open('students_password.csv', 'w', encoding = "UTF-8")
for i in range(0, len(St)):
    File1.write(str(St[i][0])+','+str(St[i][1])+','+str(St[i][2])+','+str(St[i][3])+','+str(St[i][4])+','+str(St[i][5])+','+str(St[i][6]))

File.close()
File1.close()
    
                
                
