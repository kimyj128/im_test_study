# 미로1
# bfs, queue

from collections import deque

for _ in range(10):
    test_case = int(input())

    N = 16
    mat = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mat[i][j] == '2':
                s = (i, j)
            elif mat[i][j] == '3':
                e = (i, j)

    queue = deque()
    queue.append(s)
    visited = [[0] * N for _ in range(N)]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    while queue:
        tmp = queue.popleft()
        for d in range(4):
            next_row = tmp[0] + dr[d]
            next_col = tmp[1] + dc[d]
            if next_row >= N or next_row < 0 or next_col >= N or next_col < 0:
                continue
            if mat[next_row][next_col] == '1' or visited[next_row][next_col] == 1:
                continue

            visited[next_row][next_col] = 1
            queue.append((next_row, next_col))

    print('#{} {}'.format(test_case, visited[e[0]][e[1]]))
