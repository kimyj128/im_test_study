# 숫자 배열 회전

T = int(input())

def turn90(arr, n):
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[n-1-j][i]

    return tmp
"""
    0 0 : 2 0
    0 1 : 1 0
    0 2 : 0 0
    1 0 : 2 1
"""

for test_case in range(1, 1 + T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    t90 = turn90(arr, N)
    t180 = turn90(t90, N)
    t270 = turn90(t180, N)

    print('#{}'.format(test_case))


    for i in range(N):
        tmp = ''
        for j in range(N):
            tmp += str(t90[i][j])
        tmp += ' '
        for j in range(N):
            tmp += str(t180[i][j])
        tmp += ' '
        for j in range(N):
            tmp += str(t270[i][j])

        print(tmp)


