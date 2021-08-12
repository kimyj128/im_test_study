#저울

N = int(input())
weight = list(map(int, input().split()))

# 표현 가능한 무게의 집합
numbers = set()

weight.sort()

# 무게가 너무 커서 결과에 영향을 주지 못하는 weight들 제거
cnt = 0
for i in range(len(weight)):
    if cnt < weight[i]-1:
        weight = weight[:i]
        break
    cnt += weight[i]

print(sum(weight)+1)

#-------------------------------------------------------
# 완전 탐색... 쓸데없는 코드
# # numbers에 숫자들 추가
# for w in weight:
#     tmp_set = list(numbers)
#     for num in tmp_set:
#         numbers.add(num+w)
#
#     numbers.add(w)
#
#     # 빈 자리 발견시 결과 출력
#     if len(numbers) != max(numbers):
#         tmp = 1
#
#         for r in sorted(list(numbers)):
#             if tmp != r:
#                 print(tmp)
#                 exit()
#             tmp += 1
#
# # 아무일 없이 진행되면 모든 무게 추 합+1 출력
