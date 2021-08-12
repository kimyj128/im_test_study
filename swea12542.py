# 색칠하기

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    squares = []
    for _ in range(N):
        squares.append(list(map(int, input().split())))

    arr = []
    for _ in range(10):
        arr.append([0]*10)

    for k in range(N):
        for i in range(squares[k][2] - squares[k][0] + 1):
            for j in range(squares[k][3] - squares[k][1] + 1):
                if arr[i + squares[k][0]][j + squares[k][1]] != squares[k][4]:
                    arr[i + squares[k][0]][j + squares[k][1]] += squares[k][4]

    result = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] > 2:

                result += 1

    print(f'#{test_case} {result}')