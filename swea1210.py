#Ladder1
"""
사다리를 거꾸로 탐색
위로 진행하다가 좌우에 길이 있으면 좌우로 진행
"""

for _ in range(1, 11):
    test_case = int(input())

    matrix = []

    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    # find 2
    j_idx = 0
    for i in range(100):
        if matrix[99][i] == 2:
            j_idx = i

    i_idx = 99

    while i_idx > 0:
        if 0 < j_idx and matrix[i_idx][j_idx - 1] == 1:
            matrix[i_idx][j_idx] = 0
            j_idx -= 1
            continue
        elif j_idx < 99 and matrix[i_idx][j_idx + 1] == 1:
            matrix[i_idx][j_idx] = 0
            j_idx += 1
            continue
        else:
            i_idx -= 1

    print(f'#{test_case} {j_idx}')