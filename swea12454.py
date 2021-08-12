#전기버스
T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    bus_stop = [0]*(N+1)

    for c in charge:
        bus_stop[c] = 1

    bus = K
    result = 0
    able = True
    while bus < N:

        for i in range(K):
            if bus_stop[bus-i] == 1:
                result += 1
                bus = bus-i
                
                break
        else:
            able = False
            break

        bus += K

    if able:
        print(f'#{test_case} {result}')
    else:
        print(f'#{test_case} {0}')