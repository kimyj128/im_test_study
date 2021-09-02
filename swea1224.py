# 계산기3

for test_case in range(1, 11):
    N = int(input())
    ans = input().rstrip()
    tmp = []
    stack = []

    for i in range(N):
        if ans[i] == '(':
            stack += [ans[i]]
        elif ans[i] == ')':
            while stack[-1] != '(':
                tmp += [stack.pop(-1)]
            stack.pop()
            if len(stack) != 0:
                if stack[-1] == '*' or stack[-1] == '/':
                    tmp += [stack.pop(-1)]
        elif ans[i] == '*' or ans[i] == '/':
            stack += [ans[i]]
        elif ans[i] == '+' or ans[i] == '-':
            if len(stack) != 0:
                if stack[-1] == '+' or stack[-1] == '-':
                    tmp += [stack.pop(-1)]
            stack += [ans[i]]

        else:
            tmp += [ans[i]]
            if len(stack) != 0:
                if stack[-1] == '*' or stack[-1] == '/':
                    tmp += [stack.pop(-1)]

    while len(stack) > 0:
        if stack[-1] == '(':
            stack.pop(-1)
        else:
            tmp += [stack.pop(-1)]

    N = len(tmp)
    k = 0
    while N != 1:
        if tmp[k] == '*':
            tmp = tmp[0:k - 2] + [str(int(tmp[k - 2]) * int(tmp[k - 1]))] + tmp[k+1:N]
            N -= 2
            k -= 2
        elif tmp[k] == '+':
            tmp = tmp[0:k - 2] + [str(int(tmp[k - 2]) + int(tmp[k - 1]))] + tmp[k + 1:N]
            N -= 2
            k -= 2
        k += 1
    
    print('#{} {}'.format(test_case, tmp[0]))
