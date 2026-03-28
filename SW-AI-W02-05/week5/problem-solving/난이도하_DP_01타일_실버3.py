# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys
input = sys.stdin.readline

n = int(input())

def tile(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, (a + b) % 15746
    
    return b

print(tile(n))