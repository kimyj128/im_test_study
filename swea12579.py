#앞글자따기
#아스키코드값을 변화시켜 대소문자 변경하는 문제

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = input().split()

    result = ''
    for i in range(N):
        result += chr(ord(arr[i][0])-32).upper()

    print(f'#{test_case} {result}')