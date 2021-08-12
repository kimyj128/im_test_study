#이진탐색

T = int(input())

for test_case in range(1, 1 + T):
    P, A, B = map(int, input().split())

    A_start = 1
    A_end = P
    B_start = 1
    B_end = P
    result = ''
    while True:
        A_half = int((A_start + A_end)/2)
        B_half = int((B_start + B_end)/2)
        
        if A == A_half:
            result += 'A'
        elif A > A_half:
            A_start = A_half
        else:
            A_end = A_half
            
        if B == B_half:
            result += 'B'
        elif B > B_half:
            B_start = B_half
        else:
            B_end = B_half
        
        if result == 'AB':
            print(f'#{test_case} {0}')
            break
        elif result == 'A' or result == 'B':
            print(f'#{test_case} {result}')
            break
            
            