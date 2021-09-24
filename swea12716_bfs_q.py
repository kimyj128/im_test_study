# 미로의 거리
# bfs
# queue

from collections import deque

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    mat = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mat[i][j] == '2':
                s = (i, j)
            elif mat[i][j] == '3':
                g = (i, j)

    visited = [[0] * N for _ in range(N)]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    queue = deque()
    queue.append(s)
    visited[s[0]][s[1]] = 1
    while len(queue) != 0:
        tmp = queue.popleft()
        for d in range(4):
            next_row = tmp[0] + dr[d]
            next_col = tmp[1] + dc[d]
            if next_row >= N or next_row < 0 or next_col >= N or next_col < 0 or visited[next_row][next_col] != 0 or mat[next_row][next_col] == '1':
                continue

            visited[next_row][next_col] = visited[tmp[0]][tmp[1]] + 1
            queue.append((next_row, next_col))

    if visited[g[0]][g[1]] == 0:
        visited[g[0]][g[1]] = 2
    print('#{} {}'.format(test_case, visited[g[0]][g[1]] - 2))
