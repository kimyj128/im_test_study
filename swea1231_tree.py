# 중위순회
# tree

for test_case in range(1, 11):
    V = int(input())

    data = [input().split() for _ in range(V)]

    ans = ''

    def tree(n):
        if 0 < n < V + 1:
            global ans
            if len(data[n-1]) >= 3:
                tree(int(data[n-1][2]))
            ans += '{}'.format(data[n - 1][1])
            if len(data[n-1]) == 4:
                tree(int(data[n-1][3]))

    tree(1)
    print('#{} {}'.format(test_case, ans))
