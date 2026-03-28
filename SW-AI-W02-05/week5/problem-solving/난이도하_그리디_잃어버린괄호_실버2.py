# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

expression = input()
result = 0

a = expression.split('-')   

for i in range(len(a)):
    group_sum = sum(map(int, a[i].split('+')))

    if i == 0:
        result += group_sum
    else:
        result -= group_sum

print(result)