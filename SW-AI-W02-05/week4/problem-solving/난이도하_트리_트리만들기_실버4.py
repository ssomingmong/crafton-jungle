# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [i for i in range(n)]

for i in range(m):
    print(0, i + 1)

for j in range(m, n - 1):
    print(j, j + 1)