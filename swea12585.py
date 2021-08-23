# 문자열비교
# issubstring

T = int(input())

for test_case in range(1, 1+T):
    str1 = input()
    str2 = input()
    len_str1 = len(str1)
    ans = 0
    for i in range(len(str2) - len_str1 + 1):
        if str1[0] == str2[i]:
            word = ''

            for j in range(len_str1):
                word += str2[i+j]

            if str1 == word:
                ans = 1

    print('#{} {}'.format(test_case, ans))