# 후위 표기법
# stack

T = int(input())

for test_case in range(1, 1 + T):
    ans = input().rstrip()
    N = len(ans)

    stack = []

    print('#{} '.format(test_case), end='')
    for i in range(N):
        if ans[i] == '(':
            stack += [ans[i]]
        elif ans[i] == ')':
            while stack[-1] != '(':
                print(stack.pop(-1), end='')
            stack.pop()
            if len(stack) != 0:
                if stack[-1] == '*' or stack[-1] == '/':
                    print(stack.pop(-1), end='')
        elif ans[i] == '*' or ans[i] == '/':
            stack += [ans[i]]
        elif ans[i] == '+' or ans[i] == '-':
            if len(stack) != 0:
                if stack[-1] == '+' or stack[-1] == '-':
                    print(stack.pop(-1), end='')
            stack += [ans[i]]

        else:
            print(ans[i], end='')
            if len(stack) != 0:
                if stack[-1] == '*' or stack[-1] == '/':
                    print(stack.pop(-1), end='')

    while len(stack) > 0:
        if stack[-1] == '(':
            stack.pop(-1)
        else:
            print(stack.pop(-1), end='')
    print()
