# 가장 빠른 문자열 타이핑
# swea1213 문제 수정해서 풀었음

T = int(input())

for test_case in range(1, 1+T):
    text, word = input().split()

    ans = 0
    M = len(word)
    N = len(text)
    pi = [0] * (M + 1)
    cnt = 0

    i = 1
    j = 0
    while i < M:
        if word[j] == word[i]:
            cnt += 1
            j += 1
        else:
            cnt = 0
            j = 0
        pi[i + 1] = cnt
        i += 1

    i = 0
    j = 0
    while i < N:
        if text[i] == word[j]:
            j += 1
            if j == M:
                ans += 1
                j = 0
        elif j != 0:
            i -= 1
            j = pi[j]

        i += 1

    print('#{} {}'.format(test_case, N - ans*(M-1)))