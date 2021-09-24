# 이진 트리 전위 순회
# tree

T = int(input())

for test_case in range(1, 1 + T):
    V = int(input())

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    for _ in range(V - 1):
        s, e = map(int, input().split())
        if left[s] == 0:
            left[s] = e
        else:
            right[s] = e
    ans = ''

    def tree(n):
        if n:
            global ans
            ans += ' {}'.format(n)
            if n < V + 1:
                tree(left[n])
                tree(right[n])

    tree(1)

    print('#{}{}'.format(test_case, ans))