# GNS
# 외계숫자 정렬하기

T = int(input())
for test_case in range(1, T+1):
    input()
    print('#{}'.format(test_case))
    numbers = input().split()
    cnt_keys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR',
                'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0,
           'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    for num in numbers:
        cnt[num] += 1

    cnt['NIN'] -= 1
    for k in cnt_keys:
        for i in range(cnt[k]):
            print(k, end=' ')

    print('NIN')




