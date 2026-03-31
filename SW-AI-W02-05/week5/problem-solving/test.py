import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
        n = int(input())

        applicate = []

        for _ in range(n):
            applicate.append(list(map(int, input().split())))

        applicate.sort()

        count = 1
        min_interview_rank = applicate[0][1]

        for i in range(1, n):
            if applicate[i][1] < min_interview_rank:
                count += 1
                min_interview_rank = applicate[i][1]

        print(count)