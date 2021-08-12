#숫자를 정렬하자
#버블소트

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N):
        for j in range(N - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = ''
    for num in numbers:
        result += str(num) + ' '

    print(f'#{test_case} {result.rstrip()}')