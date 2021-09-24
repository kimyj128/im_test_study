# 배열 최소합
# dfs 백트래킹

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min = 10000000
    def dfs(row, cnt):
        global min
        if row == N:
            if min > cnt:
                min = cnt
        elif cnt < min:
            for i in range(N):
                if visited[i] == 0:
                    visited[i] = 1
                    dfs(row + 1, cnt + mat[row][i])
                    visited[i] = 0

    dfs(0, 0)

    print('#{} {}'.format(test_case, min))