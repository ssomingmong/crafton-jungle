# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    applicants = []

    for _ in range(n):
        applicants.append(list(map(int, input().split())))

    applicants.sort()
    count = 1
    min_interview_rank = applicants[0][1]

    for i in range(1, n):
        if applicants[i][1] < min_interview_rank:
            count += 1
            min_interview_rank = applicants[i][1]

    print(count)