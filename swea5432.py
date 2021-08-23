#쇠막대기 자르기

T = int(input())

for test_case in range(1, 1+T):
    arr = input()
    N = len(arr)
    arr2 = []
    for i in range(N - 1):
        arr2 += [arr[i] + arr[i+1]]
    arr3 = []
    now = 0
    stk = 0
    for e in arr:
        if e == '(':
            now += 1
            stk += 1
        else:
            now -= 1
        arr3 += [now]

    ans = 0
    lsr = 0
    for i in range(N - 1):
        if arr2[i] == '()':
            lsr += 1
            ans += arr3[i+1]
    print('#{} {}'.format(test_case, ans + stk - lsr))