#String
#특정 문자열 개수 찾는 문제
#KMP

for _ in range(10):
    test_case = int(input())
    word = input()
    text = input()
    ans = 0
    N = len(word)
    M = len(text)
    pi = [0]*(N+1)
    cnt = 0
    
    i = 1
    j = 0
    while i < N:
        if word[j] == word[i]:
            cnt += 1
            j += 1
        else:
            cnt = 0
            j = 0
        pi[i+1] = cnt
        i += 1
    
    i = 0
    j = 0
    while i < M:
        if text[i] == word[j]:
            j += 1
            if j == N:
                ans += 1
                j = pi[j]
        elif j != 0:
            i -= 1
            j = pi[j]
            
        i += 1
        
    print('#{} {}'.format(test_case, ans))