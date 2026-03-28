# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

n , k = map(int, input().split())
coins = []
count = 0

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in coins:
    count += k // i
    k = k % i

print(count)