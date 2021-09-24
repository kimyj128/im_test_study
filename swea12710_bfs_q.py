# 노드의 거리
# bfs
# queue

from collections import deque

T = int(input())

for test_case in range(1, 1 + T):
    V, E = map(int, input().split())

    mat = [[] for _ in range(V + 1)]

    for _ in range(E):
        s, g = map(int, input().split())
        mat[s].append(g)
        mat[g].append(s)

    S, G = map(int, input().split())
    visited = [0] * 51
    queue = deque()
    queue.append(S)
    visited[S] = 1
    while len(queue) != 0:
        tmp = queue.popleft()
        for i in mat[tmp]:
            if visited[i] == 0:
                visited[i] = visited[tmp] + 1
                queue.append(i)
    
    if visited[G] == 0:
        visited[G] = 1
    print('#{} {}'.format(test_case, visited[G] - 1))
