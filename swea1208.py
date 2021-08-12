# flatten

"""
boxes에서 가장 높은 값을 가장 낮은값으로 1씩 옮기는 문제
"""
for test_case in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    dump = 0
    while dump < N:
        dump += 1
        max_box = 0
        max_idx = 0
        min_box = 100
        min_idx = 0
        for i in range(100):
            if boxes[i] > max_box:
                max_box = boxes[i]
                max_idx = i
            if boxes[i] < min_box:
                min_box = boxes[i]
                min_idx = i

        if max_box == min_box:
            break
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    max_box = 0
    max_idx = 0
    min_box = 100
    min_idx = 0
    for i in range(100):
        if boxes[i] > max_box:
            max_box = boxes[i]
            max_idx = i
        if boxes[i] < min_box:
            min_box = boxes[i]
            min_idx = i

    print(f'#{test_case} {boxes[max_idx]-boxes[min_idx]}')
