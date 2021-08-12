#좌표 입력받아서 사각형 넓이 구하기

#입력 받은 좌표들을 저장할 이중 배열
a = [[],[],[],[]]

#사각형 좌표 입력받기
for i in range(4):
    a[i] = input().split()

#set 생성
recset = set()

for i in a:
    for j in range(int(i[0]), int(i[2])):
        for k in range(int(i[1]), int(i[3])):
            recset.add((j,k))
        
print(len(recset))
