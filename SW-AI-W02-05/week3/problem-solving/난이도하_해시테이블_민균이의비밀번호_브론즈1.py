# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
import sys
input = sys.stdin.readline

N = int(input())
dt = {}


for i in range(N):
    pwd = input().strip()
    dt[pwd] = pwd[::-1]
    mid = len(pwd) // 2

    if pwd[::-1] in dt :
        print(f"{len(pwd)} {pwd[mid]}")