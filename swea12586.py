# 회문

T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += board[j][i]
        board += [temp]

    for i in range(N*2):
        for j in range(N-M+1):
            tmp = board[i][j: j + M]
            if tmp == tmp[::-1]:
                print('#{} {}'.format(test_case, tmp))
