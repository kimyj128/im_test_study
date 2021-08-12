#달팽이 숫자

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    ans = []
    for j in range(N):
        ans.append([0]*N)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    d = 0
    ix = 0
    iy = 0
    for i in range(1, N**2 + 1):
        ans[iy][ix] = i

        if 0 <= ix + dx[d] < N and 0 <= iy + dy[d] < N and ans[iy + dy[d]][ix + dx[d]] == 0:
            pass
        else:
            d = (d + 1) % 4
        ix += dx[d]
        iy += dy[d]


    print(f'#{test_case}')
    for i in range(N):
        result = ''
        for j in range(N):
            result += str(ans[i][j])
            result += ' '

        print(result.rstrip())