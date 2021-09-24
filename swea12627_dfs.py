# 그래프 경로
# dfs

T = int(input())

for test_case in range(1, 1+T):
    V, E = map(int, input().split())

    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1

    start, end = map(int, input().split())
    visited = [0]*(V+1)
    visited[start] = 1

    def dfs(now):
        for next in range(1, V+1):
            if adj[now][next] == 1 and visited[next] == 0:
                visited[next] = 1
                dfs(next)

    dfs(start)
    print('#{} {}'.format(test_case, visited[end]))