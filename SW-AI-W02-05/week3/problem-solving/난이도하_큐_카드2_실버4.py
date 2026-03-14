# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque

N = int(input())
cards = [i+1 for i in range(N)]
queue = deque(cards)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])