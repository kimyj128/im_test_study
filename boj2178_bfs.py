# 미로 탐색
# bfs
# queue

from collections import deque

N, M = map(int, input().split())
mat = [input() for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
queue = deque()
queue.append((0, 0))
visited[0][0] = 1
while len(queue) != 0:
    tmp = queue.popleft()
    for d in range(4):
        next_row = tmp[0] + dr[d]
        next_col = tmp[1] + dc[d]
        if next_row >= N or next_row < 0 or next_col >= M or next_col < 0 or visited[next_row][next_col] != 0 or mat[next_row][next_col] == '0':
            continue

        visited[next_row][next_col] = visited[tmp[0]][tmp[1]] + 1
        queue.append((next_row, next_col))

print(visited[N - 1][M - 1])
