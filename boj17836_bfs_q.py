# 공주님을 구해라!
# bfs
# queue

from collections import deque

# 입력받는 부분
N, M, T = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
mat[0][0] = 1

gram = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
queue = deque()
queue.append((0, 0))

# 시간 저장하기
time = [[0] * M for _ in range(N)]

# bfs진행
while len(queue) != 0:
    tmp = queue.popleft()
    for d in range(4):
        next_row = tmp[0] + dr[d]
        next_col = tmp[1] + dc[d]
        if next_row >= N or next_row < 0 or next_col >= M or next_col < 0 or mat[next_row][next_col] == 1:
            continue

        if mat[next_row][next_col] == 2:
            gram = (next_row, next_col)
        mat[next_row][next_col] = 1
        time[next_row][next_col] = time[tmp[0]][tmp[1]] + 1
        queue.append((next_row, next_col))


T2 = time[N - 1][M - 1]
T1 = T2 + 1
if T2 == 0 and gram == 0:
    T = -1
elif gram == 0:
    pass
elif T2 == 0:
    T1 = time[gram[0]][gram[1]] + M - gram[1] + N - gram[0] - 2
    T2 = T1 + 1
else:
    T1 = time[gram[0]][gram[1]] + M - gram[1] + N - gram[0] - 2

if min(T1, T2) > T:
    ans = 'Fail'
else:
    ans = min(T1, T2)

print(ans)

