# 스택연습

T = int(input().rstrip())

for test_case in range(1, 1+T):
    N = int(input().rstrip())

    top = 0
    data = []
    print('#{}'.format(test_case))
    for _ in range(N):
        command = input().rstrip()

        if command[0] == 'i':
            data.append(int(command[2:]))
            top += 1
        elif command[0] == 'c':
            print(top)
        else:
            if top == 0:
                print('empty')
            else:
                print(data.pop(-1))
                top -= 1