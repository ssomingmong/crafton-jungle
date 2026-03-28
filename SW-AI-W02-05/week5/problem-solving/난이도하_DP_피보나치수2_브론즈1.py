# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

import sys
input = sys.stdin.readline

n = int(input())
fibo_dp = {0:0, 1:1}

def fibo(n):
    if n in fibo_dp:
        return fibo_dp[n]
    
    nth_dp = fibo(n - 1) + fibo(n - 2)
    fibo_dp[n] = nth_dp

    return nth_dp

print(fibo(n))