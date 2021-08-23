# 비밀번호
# 반복문자 제거

for test_case in range(1, 11):

    N, text = map(str, input().split())
    N = int(N)
    i = 0
    while i < N-1:
        if text[i] == text[i + 1]:
            if i + 2 < N:
                text = text[0:i] + text[i+2:]
            else:
                text = text[0:i]
            if i != 0:
                i -= 1
            N -= 2
        else:
            i += 1

    print('#{} {}'.format(test_case, text))

