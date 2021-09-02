# 암호생성기
# queue


def POP(arr, f):
    tmp = arr[f]
    arr[f] = 0
    return tmp


def ADD(arr, r, val):
    arr[r] = val


for _ in range(10):
    test_case = int(input())
    numbers = list(map(int, input().split()))

    numbers += [0]
    front = 0
    rear = 7
    i = 1
    while True:
        rear = (rear + 1) % 9
        pop_num = POP(numbers, front) - i
        front = (front + 1) % 9
        i = (i % 5) + 1
        if pop_num <= 0:
            ADD(numbers, rear, 0)
            break
        ADD(numbers, rear, pop_num)

    ans = ''
    for _ in range(8):
        ans += ' {}'.format(numbers[front])
        front = (front + 1) % 9

    print('#{}{}'.format(test_case, ans))



