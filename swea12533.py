#델타검색 응용

for test_case in range(1, 11):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    di = [-2, 2, -2, 2, 1, 1, -1, -1]
    dj = [1, 1, -1, -1, -2, 2, -2, 2]
    cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 0 or ni > N - 1 or nj < 0 or nj > N - 1:
                    continue

                tmp = arr[ni][nj] - arr[i][j]
                if tmp > 0:
                    cnt += tmp
                else:
                    cnt -= tmp
    print(f'#{test_case} {cnt}')