# 알파벳
# dfs
# DAT

import sys

row, col = map(int, sys.stdin.readline().split())

board = []
for _ in range(row):
    board += [sys.stdin.readline()]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
visited = [0] * 256
visited[ord(board[0][0])] = 1
ans = 1

def dfs(r, c, a):
    de = 1
    global ans
    for d in range(4):
        if 0 <= r + dr[d] < row and 0 <= c + dc[d] < col:
            next_r = r + dr[d]
            next_c = c + dc[d]
            if visited[ord(board[next_r][next_c])] == 0:
                visited[ord(board[next_r][next_c])] = 1
                dfs(next_r, next_c, a + 1)
                visited[ord(board[next_r][next_c])] = 0

    if ans < a:
        ans = a


dfs(0, 0, 1)

print(ans)
