# 등수 찾기
# 완전탐색
# bfs, queue

from collections import deque
import sys

N, M, X = map(int, input().split())

mat1 = [[] for _ in range(N + 1)]
mat2 = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    mat1[a].append(b)
    mat2[b].append(a)

queue1 = deque()
queue2 = deque()

queue1.append(X)
queue2.append(X)
back = 0
front = 0

visited = [0] * (N + 1)
while len(queue1) != 0:
    tmp = queue1.popleft()

    for i in mat1[tmp]:
        if visited[i] == 0:
            visited[i] = 1
            back += 1
            queue1.append(i)
while len(queue2) != 0:
    tmp = queue2.popleft()

    for i in mat2[tmp]:
        if visited[i] == 0:
            visited[i] = 1
            front += 1
            queue2.append(i)

ans1 = front + 1
ans2 = N - back

print('{} {}'.format(ans1, ans2))
