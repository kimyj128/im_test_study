# 부분 집합의 합

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr01 = [1]*N + [0]*(12-N)
    result = 0

    while True:
        arr_sum = 0
        cnt = 0
        for i in range(12):
            if arr01[i] == 1:
                arr_sum += arr01[i]
                cnt += i+1
        if arr_sum == N and cnt == K:
            result += 1
        arr01[0] += 1
        for i in range(11):
            if arr01[i] == 2:
                arr01[i] = 0
                arr01[i + 1] += 1
            else:
                break
        if arr01[11] == 2:
            break

    print(f'#{test_case} {result}')



