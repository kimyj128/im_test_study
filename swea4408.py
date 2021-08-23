# 자기 방으로 돌아가기

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())

    start_end = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        start_end[i][0] = (start_end[i][0] + 1)//2
        start_end[i][1] = (start_end[i][1] + 1)//2
    room = [0]*201

    for i in start_end:
        j = i[0]
        k = i[1]
        if j > k:
            j, k = k, j
        while j <= k:
            room[j] += 1
            j += 1

    ans = 0
    for r in room:
        if ans < r:
            ans = r

    print('#{} {}'.format(test_case, ans))