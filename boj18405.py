# 경쟁적 감염
# bfs
# queue

from collections import deque

# 입력받는 부분
N, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 해당 좌표가 0이 아니면 바로 해당좌표값이 정답!
if mat[X - 1][Y - 1] == 0:
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    queue = deque()


    tmp = [[] for _ in range(K + 1)]
    # 먼저 입력된 바이러스가 먼저 처리되므로 1부터 큐에 넣기
    for i in range(N):
        for j in range(N):
            if mat[i][j] != 0:
                tmp[mat[i][j]].append((i, j))
    for i in range(1, 1 + K):
        for j in range(len(tmp[i])):
            queue.append(tmp[i][j])

    # 시간 저장하기
    time = [[0] * N for _ in range(N)]

    # bfs진행
    while len(queue) != 0:
        tmp = queue.popleft()
        for d in range(4):
            next_row = tmp[0] + dr[d]
            next_col = tmp[1] + dc[d]
            if next_row >= N or next_row < 0 or next_col >= N or next_col < 0 or mat[next_row][next_col] != 0:
                continue

            mat[next_row][next_col] = mat[tmp[0]][tmp[1]]
            time[next_row][next_col] = time[tmp[0]][tmp[1]] + 1
            queue.append((next_row, next_col))

    # 해당 좌표가 S보다 나중에 전염되었으면 0
    if time[X - 1][Y - 1] > S:
        ans = 0
    else:
        ans = mat[X - 1][Y - 1]
else:
    ans = mat[X - 1][Y - 1]


print(ans)

