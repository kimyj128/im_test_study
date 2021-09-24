# 피자 굽기
# queue

T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    queue = []

    i = 0
    ans = -1
    while True:
        if len(queue) < N:
            if i < M:
                queue.append([pizza[i], i + 1])
                i += 1
                continue

        if len(queue) == 0:
            ans = p[1]
            break

        p = queue.pop(0)
        p[0] //= 2
        if p[0] == 0:
            continue

        queue.append(p)

    print('#{} {}'.format(test_case, ans))