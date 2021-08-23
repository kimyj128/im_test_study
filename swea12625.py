# 종이붙이기
# dp


"""재귀
def stack(N):
    if N == 10:
        return 1
    elif N == 0:
        return 1
    return stack(N-10) + 2*stack(N-20)
"""
stack_arr = [1, 1]
for i in range(29):
    stack_arr += [stack_arr[i]*2 + stack_arr[i+1]]

T = int(input())
for test_case in range(1, 1+T):
    N = int(input())

    print('#{} {}'.format(test_case, stack_arr[N//10]))