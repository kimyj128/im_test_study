# 학생들이 버튼 누르는 문제

switchs = int(input())
switch = input().split()

students = []
school = int(input())
for i in range(school):
    tmp = input().split()
    students.append([int(tmp[0]),int(tmp[1])-1])

def change_switch(b):
    a = int(b)
    a += 1
    a %= 2 
    return str(a)

for student in students:
    if student[0] == 1:
        
        for i in range(switchs):
            if (i+1)%(student[1]+1) == 0:
                switch[i] = change_switch(switch[i])
    else:
        i = 0
        switch[student[1]] = change_switch(switch[student[1]])
        while True:
            
            if student[1]-i < 0:
                break
            elif student[1]+i > switchs-1:
                break
            elif switch[student[1]+i] == switch[student[1]-i]:
                
                switch[student[1]+i] = change_switch(switch[student[1]+i])
                switch[student[1]-i] = change_switch(switch[student[1]-i])
            else:
                break

            i += 1            

result = ''
for i in range(switchs):
    result += str(switch[i])
    if i % 20 == 19:
        result += '\n'
    else:
        result += ' '
print(result)