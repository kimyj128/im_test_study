# 글자 수

T = int(input())

for test_case in range(1, 1+T):
    str1 = input()
    str2 = input()

    str1_arr = []
    for s in str1:
        str1_arr += [s]

    list(set(str1_arr))
    M = len(str1_arr)
    cnt = [0]*M

    for s in str2:
        for i in range(M):
            if s == str1_arr[i]:
                cnt[i] += 1

    maximum = 0
    for i in range(M):
        if maximum < cnt[i]:
            maximum = cnt[i]

    print('#{} {}'.format(test_case, maximum))

