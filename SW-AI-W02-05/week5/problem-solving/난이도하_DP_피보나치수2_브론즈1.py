# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

import sys
input = sys.stdin.readline


n = int(input())    # n번째  피보나치 수를 구하기 위한 입력

# 메모제이션 딕셔너리: 이미 계산한 피보나치 값을 저장
# fib(0) = 0, fib(1) = 1 을 초기값으로 설정
fibo_dp = {0:0, 1:1}

def fibo(n):
    if n in fibo_dp:
        return fibo_dp[n]
    
    # 아직 계산 안 한 경우: 재귀로 n - 1, n - 2 값을 구해 합산(Top-down dp)
    nth_dp = fibo(n - 1) + fibo(n - 2)

    # 계산한 값을 딕셔너리에 저장
    fibo_dp[n] = nth_dp

    return nth_dp

print(fibo(n))