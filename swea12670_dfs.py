# 미로
# dfs

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    mat = ['1' * (N + 2)]
    mat += ['1' + input().rstrip() + '1' for _ in range(N)]
    mat += ['1' * (N + 2)]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    visitable = [['0'] * (N + 2) for _ in range(N + 2)]
    ans = 0
    for i in range(N+2):
        for j in range(N+2):
            visitable[i][j] = mat[i][j]
            if mat[i][j] == '2':
                start_i = i
                start_j = j

    def go(i, j):
        global ans

        if mat[i][j] == '3':
            ans = 1
            for ii in range(N + 2):
                for jj in range(N + 2):
                    visitable[ii][jj] = '1'
            return

        visitable[i][j] = '1'
        for d in range(4):
            if visitable[i + dr[d]][j + dc[d]] != '1':
                go(i + dr[d], j + dc[d])

    go(start_i, start_j)
    print('#{} {}'.format(test_case, ans))
