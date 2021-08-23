# 파스칼의 삼각형

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())

    data = [[0, 1, 0]]
    print('#{}'.format(test_case))
    for i in range(N-1):
        tmp = [0]
        for j in range(i+2):
            tmp += [data[i][j]+data[i][j+1]]
        tmp += [0]
        data += [tmp]

    for d in data:
        tmp = ''
        for i in range(len(d)-2):
            tmp += f'{d[i+1]} '

        print(tmp.rstrip())

