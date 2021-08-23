# 오목
# dr dc 안써서 코드가 쓸데없이 길어짐

mat = [list(map(int, input().split())) for _ in range(19)]

# dp[19][19][4] 배열 생성
dp_1 = [[[0]*4 for _ in range(19)] for _ in range(19)]
dp_2 = [[[0]*4 for _ in range(19)] for _ in range(19)]

# 바둑판에 돌이 있으면 해당 돌입력(모든 방향으로 1)
for i in range(19):
    for j in range(19):
        if mat[i][j] == 1:
            for k in range(4):
                dp_1[i][j][k] = 1
        if mat[i][j] == 2:
            for k in range(4):
                dp_2[i][j][k] = 1
# 바둑판에 돌이 있으면 이전 위치에 있는 dp에 +1
for j in range(18, -1, -1):
    for i in range(18, -1, -1):
        if mat[i][j] == 1:
            if j+1 < 19:
                dp_1[i][j][0] += dp_1[i][j+1][0]
            if i < 18 and j < 18:
                dp_1[i][j][1] += dp_1[i+1][j+1][1]
            if i < 18:
                dp_1[i][j][2] += dp_1[i+1][j][2]
            if j < 18 and i > 0:
                dp_1[i][j][3] += dp_1[i-1][j+1][3]
        if mat[i][j] == 2:
            if j+1 < 19:
                dp_2[i][j][0] += dp_2[i][j+1][0]
            if i < 18 and j < 18:
                dp_2[i][j][1] += dp_2[i+1][j+1][1]
            if i < 18:
                dp_2[i][j][2] += dp_2[i+1][j][2]
            if j < 18 and i > 0:
                dp_2[i][j][3] += dp_2[i-1][j+1][3]

winner = 0
# 5개일 경우 x, y 인덱스 저장
for i in range(19):
    for j in range(19):
        if dp_1[i][j][0] == 5:
            if j == 0:
                winner = 1
                x = i + 1
                y = j + 1
            elif dp_1[i][j-1][0] != 6:
                winner = 1
                x = i + 1
                y = j + 1
        if dp_1[i][j][1] == 5:
            if j == 0 or i == 0:
                winner = 1
                x = i + 1
                y = j + 1
            elif dp_1[i-1][j-1][1] != 6:
                winner = 1
                x = i + 1
                y = j + 1
        if dp_1[i][j][2] == 5:
            if i == 0:
                winner = 1
                x = i + 1
                y = j + 1
            elif dp_1[i-1][j][2] != 6:
                winner = 1
                x = i + 1
                y = j + 1
        if dp_1[i][j][3] == 5:
            if j == 0 or i == 18:
                winner = 1
                x = i + 1
                y = j + 1
            elif dp_1[i+1][j-1][3] != 6:
                winner = 1
                x = i + 1
                y = j + 1
        if dp_2[i][j][0] == 5:
            if j == 0:
                winner = 2
                x = i + 1
                y = j + 1
            elif dp_2[i][j-1][0] != 6:
                winner = 2
                x = i + 1
                y = j + 1
        if dp_2[i][j][1] == 5:
            if j == 0:
                winner = 2
                x = i + 1
                y = j + 1
            elif dp_2[i-1][j-1][1] != 6:
                winner = 2
                x = i + 1
                y = j + 1
        if dp_2[i][j][2] == 5:
            if i == 0:
                winner = 2
                x = i + 1
                y = j + 1
            elif i > 0 and dp_2[i-1][j][2] != 6:
                winner = 2
                x = i + 1
                y = j + 1
        if dp_2[i][j][3] == 5:
            if j == 0 or i == 18:
                winner = 2
                x = i + 1
                y = j + 1
            elif dp_2[i+1][j-1][3] != 6:
                winner = 2
                x = i + 1
                y = j + 1


if winner == 0:
    print('{}'.format(winner))
else:
    print('{}'.format(winner))
    print('{} {}'.format(x, y))
