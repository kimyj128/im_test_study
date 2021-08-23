# 삼성시의 버스 노선

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    start_end = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    cnt = [0]*len(bus_stop)
    i = 0
    for bs in bus_stop:
        for se in start_end:
            if se[0] <= bs <= se[1]:
                cnt[i] += 1
        i += 1
    ans = ''
    for c in cnt:
        ans += f' {c}'

    print('#{}{}'.format(test_case, ans))