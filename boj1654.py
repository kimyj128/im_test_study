K, N = map(int, input().split())
numbers = []
for i in range(K):
    numbers.append(int(input()))

"""
대략적인 정답 유추하기
모든 랜선을 더해서 N으로 나눠본다.
그리딩을 통해 탐색횟수를 일정 이하로 줄여준다.
"""
all_sum = 0
for num in numbers:
    all_sum += num

ans = all_sum//N

while True:
    tmp = ans//2
    if tmp == 0:
        break
    n = 0
    for num in numbers:
        n += num//tmp
    if n >= N:
        break
    ans = tmp
if ans > 1000000:
    while True:
        tmp = ans - 100000
        if tmp == 0:
            break
        n = 0
        for num in numbers:
            n += num//tmp
        if n >= N:
            break
        ans = tmp
if ans > 10000:
    while True:
        tmp = ans - 1000
        if tmp == 0:
            break
        n = 0
        for num in numbers:
            n += num//tmp
        if n >= N:
            break
        ans = tmp

while True:
    n = 0
    for num in numbers:
        n += num//ans
    if n >= N:
        print(ans)
        break
    else:
        ans -= 1
