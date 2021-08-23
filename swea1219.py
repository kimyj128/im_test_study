# 길찾기
# 재귀스택

for _ in range(10):
    test_case, N = map(int, input().split())
    trash = list(map(int, input().split()))

    way1 = [-1]*100
    way2 = [-1]*100

    for i in range(N):
        if way1[trash[2 * i]] == -1:
            way1[trash[2 * i]] = trash[2 * i + 1]
        else:
            way2[trash[2 * i]] = trash[2 * i + 1]


    ans = 0
    def go(now):
        if now == 99:
            global ans
            ans = 1
            return

        elif now != -1:
            go(way1[now])
            way1[now] = -1
            go(way2[now])
            way2[now] = -1

    go(0)
    print('#{} {}'.format(test_case, ans))

