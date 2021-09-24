# 토마토
# bfs
# queue

from collections import deque

M, N = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
queue = deque()
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            queue.append((i, j))

while len(queue) != 0:
    tmp = queue.popleft()
    for d in range(4):
        next_row = tmp[0] + dr[d]
        next_col = tmp[1] + dc[d]
        if next_row >= N or next_row < 0 or next_col >= M or next_col < 0 or mat[next_row][next_col] != 0:
            continue

        mat[next_row][next_col] = mat[tmp[0]][tmp[1]] + 1
        queue.append((next_row, next_col))

ans = 0
flag = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            flag = 1
        else:
            if ans < mat[i][j]:
                ans = mat[i][j]
if flag == 1:
    ans = -1
else:
    ans -= 1
print(ans)
