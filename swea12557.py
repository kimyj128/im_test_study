#특별한 정렬

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0
    for i in range(N):
        if i % 2:
            minimum = 101
            for j in range(i, N):
                if minimum > numbers[j]:
                    minimum = numbers[j]
                    min_idx = j
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        else:
            maximum = 0
            for j in range(i, N):
                if maximum < numbers[j]:
                    maximum = numbers[j]
                    max_idx = j
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
    result = ''
    for i in range(10):
        result += str(numbers[i]) + ' '
    print(f'#{test_case} {result.rstrip()}')