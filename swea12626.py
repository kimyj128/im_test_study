# 괄호검사
# 스택

T = int(input())

for test_case in range(1, 1+T):
    text = input()

    stack = []
    top = -1
    ans = 1
    for t in text:
        if t == '(' or t == '{':
            stack += [t]
            top += 1
        elif t == ')':
            if top >= 0 and stack[top] == '(':
                stack.pop(-1)
                top -= 1
            else:
                ans = 0
                break
        elif t == '}':
            if top >= 0 and stack[top] == '{':
                stack.pop(-1)
                top -= 1
            else:
                ans = 0
                break

    if top != -1:
        ans = 0
    print('#{} {}'.format(test_case, ans))