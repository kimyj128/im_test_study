# Forth
# 후위표기법 계산
# stack

T = int(input())

for test_case in range(1, 1 + T):
    tmp = input().rstrip().split()
    N = len(tmp)
    stack = []

    try:
        for k in range(N-1):
            if tmp[k] == '*':
                stack += [stack.pop(-1) * stack.pop(-1)]
            elif tmp[k] == '+':
                stack += [stack.pop(-1) + stack.pop(-1)]
            elif tmp[k] == '/':
                n1 = stack.pop(-1)
                n2 = stack.pop(-1)
                stack += [n2 // n1]
            elif tmp[k] == '-':
                n1 = stack.pop(-1)
                n2 = stack.pop(-1)
                stack += [n2 - n1]
            else:
                stack += [int(tmp[k])]
    except:
        print('#{} error'.format(test_case))
        continue

    if len(stack) == 1 and tmp[-1] == '.':
        print('#{} {}'.format(test_case, stack[0]))
    else:
        print('#{} error'.format(test_case))