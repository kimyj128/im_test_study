#모음이 보이지 않는 사람

T = int(input())

for test_case in range(1, T+1):
    word = input()
    result = ''
    for w in word:
        if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
            continue
        result += w
    print('#{} {}'.format(test_case, result))