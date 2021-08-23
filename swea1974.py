# 스도쿠 검증

T = int(input())

for test_case in range(1, 1 + T):
    ans = 0
    arr = [list(map(int, input().split())) for _ in range(9)]
    check = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(9):
        check_row = [0]*10
        check_col = [0]*10
        check_sqr = [0]*10
        for j in range(9):
            check_row[arr[i][j]] += 1
            check_col[arr[j][i]] += 1
            check_sqr[arr[(i//3)*3 + j//3][(i%3)*3 + j%3]] += 1
        if check_row != check or check_col != check or check_sqr != check:
            break
    else:
        ans = 1

    print('#{} {}'.format(test_case, ans))