#이중배열 델타검색
for test_case in range(1, 11):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                    continue
            
                tmp = arr[ni][nj] - arr[i][j]
                if tmp > 0:
                    cnt += tmp
                else:
                    cnt -= tmp
    print(f'#{test_case} {cnt}')

#---------------------------------------------------------------------------
# 배열 외곽을 덧씌워 계산하기
# for test_case in range(1, 11):
#     N = int(input())

#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))

#     arr_padding = []
#     for _ in range(N+2):
#         arr_padding.append([0]*(N+2))

#     for i in range(N):
#         for j in range(N):
#             arr_padding[i+1][j+1] = arr[i][j]

#     for i in range(N):
#         arr_padding[0][i+1] = arr[0][i]
#         arr_padding[N+1][i+1] = arr[N-1][i]

#     for i in range(N):
#         arr_padding[i+1][0] = arr[i][0]
#         arr_padding[i+1][N+1] = arr[i][N-1]
#     cnt = 0
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             tmp = arr_padding[i][j] - arr_padding[i+1][j]
#             if tmp > 0:
#                 cnt += tmp
#             else:
#                 cnt -= tmp
#             tmp = arr_padding[i][j] - arr_padding[i][j+1]
#             if tmp > 0:
#                 cnt += tmp
#             else:
#                 cnt -= tmp
#             tmp = arr_padding[i][j] - arr_padding[i-1][j]
#             if tmp > 0:
#                 cnt += tmp
#             else:
#                 cnt -= tmp
#             tmp = arr_padding[i][j] - arr_padding[i][j-1]
#             if tmp > 0:
#                 cnt += tmp
#             else:
#                 cnt -= tmp

#     print(f'#{test_case} {cnt}')