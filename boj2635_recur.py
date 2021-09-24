#역 피보나치

#재귀함수를 이용한 방식

#사용자로부터 숫자 1개 입력받기
N = int(input())

#몇 번 실행되었는지 계산해주는 함수
def rev_fib(f1, f2, iter):
    if f1 - f2 < 0:
        return iter
    else:
        return rev_fib(f2, f1-f2, iter+1)

#숫자 두개를 입력받아 다음 수를 출력해주는 역피보나치 함수
def print_rev_fib(f1, f2):
    if f1 - f2 >= 0:
        print(f1-f2,end=' ')
        return print_rev_fib(f2, f1-f2)

#반복이 최대로 이루어 질 때의 숫자를 저장할 변수
num = 0
#최대 반복수를 저장할 변수
max_iter = 2

#1~N까지 순회하며 num, max_iter 탐색
for i in range(1,N+1):
    tmp = rev_fib(N, i, 2)
    if tmp > max_iter:
        max_iter = tmp
        num = i

print(max_iter)
print(N,end=' ')
print(num,end=' ')
print_rev_fib(N, num)
#------------------------------------------
#반복문을 이용한 방식
# N = int(input())

# def rev_fib_iter(f1, f2):
#     iter = 2
#     while f1 >= f2:
#         f1, f2 = f2, f1-f2
#         iter += 1
#     return iter

# def print_rev_fib(f1, f2):
#     while f1 >= f2:
#         f1, f2 = f2, f1-f2
#         print(f2,end=' ')
        

# num = 0
# max_iter = 0
# for i in range(1,N+1):
#     tmp = rev_fib_iter(N, i)
#     if tmp > max_iter:
#         max_iter = tmp
#         num = i

# print(max_iter)
# print(N,end=' ')
# print(num,end=' ')
# print_rev_fib(N, num)

