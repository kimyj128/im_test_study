#부분집합 합

for test_case in range(1, 11):
    N = int(input())
    numbers = list(map(int, input().split()))

    binary = [0]*N

    result = 0
    for i in range(2**N):
        cnt = 0
        for j in range(N):
            cnt += numbers[j]*binary[j]

        if cnt == 0:
            result += 1

        binary[0] += 1
        for j in range(N):
            if binary[j] > 1 and j < N-1:
                binary[j] -= 2
                binary[j+1] += 1

    print(f'#{test_case} {result}')