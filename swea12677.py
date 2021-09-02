# 토너먼트 카드 게임
# dfs

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [0]
    arr += list(map(int, input().split()))
    b_win = [(1, 2), (2, 3), (3, 1)]
    
    
    def half(i, j):
        if i == j:
            return i
        else:
            a = half(i, (i+j)//2)
            b = half((i+j)//2 + 1, j)

        if (arr[a], arr[b]) in b_win:
            return b
        return a
    print('#{} {}'.format(test_case, half(1, N)))
