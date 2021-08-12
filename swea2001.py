#파리잡기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    matrix = []

    for i in range(N):
        matrix.append(list(map(int, input().split())))
#--------------------------------------------------------------입력완료        
    MM = 0        
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for k in range(M):
                for h in range(M):
                    tmp += matrix[i+k][j+h]
                
            if tmp > MM:
                MM = tmp

    print(f'#{test_case} {MM}')