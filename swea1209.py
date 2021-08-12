# 배열중 최댓값 탐색

for _ in range(1, 11):
    test_case = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    maximum = 0
    
    cnt2 = 0
    cnt3 = 0
    for i in range(100):
        cnt2 += arr[i][i]
        cnt3 += arr[99-i][i]
        
        cnt = 0
        cnt1 = 0        
        for j in range(100):
            cnt += arr[i][j]
            cnt1 += arr[j][i]
            
        if cnt > maximum:
            maximum = cnt
        if cnt1 > maximum:
            maximum = cnt1

    if cnt2 > maximum:
        maximum = cnt2
    if cnt3 > maximum:
        maximum = cnt3    
    print(f'#{test_case} {maximum}')