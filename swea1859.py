# 백만장자 프로젝트

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    arr = list(map(int, input().split()))

    max = 0
    cnt = 0
    for i in arr[::-1]:
        if i > max:
            max = i
        else:
            cnt += max-i

    print('#{} {}'.format(test_case, cnt))