#문자열의 거울상
#bdpq 글자 대칭시키기

T = int(input())

for test_case in range(1, T+1):
    before = input()
    N = len(before)
    after = ''
    for i in range(N-1, -1, -1):
        if before[i] == 'b':
            after += chr(ord(before[i])+2)
        elif before[i] == 'd':
            after += chr(ord(before[i])-2)
        elif before[i] == 'p':
            after += chr(ord(before[i])+1)
        else:
            after += chr(ord(before[i])-1)

    print('#{} {}'.format(test_case, after))