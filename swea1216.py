# 회문2
# 100*100에서 가장 긴 회문의 길이 구하기

for _ in range(10):
    test_case = int(input())
    board = [input() for _ in range(100)]

    ans = 1
    for i in range(100):
        for j in range(100):
            cnt = 0
            while True:
                if cnt <= i < 99-cnt and board[i-cnt][j] == board[i+1+cnt][j]:
                    cnt += 1
                else:
                    break
            if ans < cnt*2:
                ans = cnt*2

            cnt = 1
            while True:
                if cnt <= i < 100-cnt and board[i-cnt][j] == board[i+cnt][j]:
                    cnt += 1
                else:
                    break
            if ans < cnt*2-1:
                ans = cnt*2-1

            cnt = 1
            while True:
                if cnt <= j < 100-cnt and board[i][j-cnt] == board[i][j + cnt]:
                    cnt += 1
                else:
                    break
            if ans < cnt*2-1:
                ans = cnt*2-1

            cnt = 0
            while True:
                if cnt <= j < 99-cnt and board[i][j - cnt] == board[i][j + 1 + cnt]:
                    cnt += 1
                else:
                    break
            if ans < cnt*2:
                ans = cnt*2

    print('#{} {}'.format(test_case, ans))
