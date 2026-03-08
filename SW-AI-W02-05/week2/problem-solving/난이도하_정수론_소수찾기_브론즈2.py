# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978


N = int(input())

arr = list(map(int, input().split()))

count = 0

for i in arr:
    if i == 1:
        continue

    isPrime = True

    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    
    if isPrime == True:
        count += 1

print(count)