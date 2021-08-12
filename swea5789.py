#현주의 상자바꾸기

T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    numlist = [0] * N

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            numlist[j] = i+1


    print(f'#{test_case} {" ".join(list(map(str, numlist)))}')
