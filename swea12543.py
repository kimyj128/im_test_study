# 부분 집합의 합
# dfs

T = int(input())

for test_case in range(1, 1 + T):
    N, K = map(int, input().split())
    ans = 0
    def dfs(now, sum, cnt):
        global ans
        if now <= 20 and sum < K and cnt < N:
            dfs(now + 1, sum, cnt)
            dfs(now + 1, sum + now, cnt + 1)
        elif sum == K and cnt == N:
            ans += 1

    dfs(1, 0, 0)

    print('#{} {}'.format(test_case, ans))