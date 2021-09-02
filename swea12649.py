# N Castle
# 백트래킹
# dfs

for test_case in range(1, 11):
    N = int(input())
    ans = 0


    def rec(row, p):
        global ans
        if row == N:
            ans += 1
            return

        for i in range(N):
            if p[i] == 0:
                p[i] = 1
                rec(row + 1, p)
                p[i] = 0

    rec(0, [0]*N)
    print('#{} {}'.format(test_case, ans))