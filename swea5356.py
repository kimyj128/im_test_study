#의석이의 세로로 말해요

T = int(input())

for test_case in range(1, 1+T):
    words = [input() for _ in range(5)]

    board = [[''] * 15 for _ in range(5)]

    i = 0
    for w in words:
        j = 0
        for c in w:
            board[i][j] = c
            j += 1
        i += 1
    ans = ''

    for k in range(15):
        for l in range(5):
            ans += board[l][k]

    print('#{} {}'.format(test_case, ans))