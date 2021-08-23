# 색상환
# dfs 

N = int(input())
K = int(input())

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    dp[i][0] = 1
    dp[i][1] = i

n = 2
while n < N+1:
    k = 1
    while k < K+1 and k <= n/2:
        if n == 2*k:
            dp[n][k] = 2
        else:
            dp[n][k] = (dp[n-2][k-1] + dp[n-1][k]) % 1000000003
        k += 1
    n += 1

print(dp[N][K])