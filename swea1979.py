# 어디에 단어가 들어갈 수 있을까
"""
주어진 퍼즐에 패딩을 적용하고
해당 퍼즐에서 '0' + '1'*K + '0'의 값을 ex)01110
가로 세로에서 찾습니다. 
"""

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    matrix = []
    result = 0
    for _ in range(N+2):
        matrix.append([0]*(N+2))

    for i in range(1, N+1):
        j = 1
        for num in map(int, input().split()):
            matrix[i][j] = num
            j += 1
    for i in range(1, N+1):
        for j in range(N - K + 1):
            if matrix[i][j] == 0:
                tmp1 = ''
                for k in range(K + 2):
                    tmp1 += str(matrix[i][j+k])
                if tmp1 == '0' + '1'*K + '0':
                    result += 1
            if matrix[j][i] == 0:
                tmp2 = ''
                for k in range(K + 2):
                    tmp2 += str(matrix[j+k][i])
                if tmp2 == '0' + '1'*K + '0':
                    result += 1

    print(f'#{test_case} {result}')