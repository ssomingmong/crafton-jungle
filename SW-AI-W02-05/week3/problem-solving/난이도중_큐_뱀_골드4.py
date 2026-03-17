#뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())  
k = int(input())  


board = [[0] * n for _ in range(n)]


for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

l = int(input())  # 방향 전환 횟수


turns = {}
for _ in range(l):
    x, c = input().split()
    turns[int(x)] = c



dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


snake = deque()
snake.append((0, 0))  


snake_set = set()
snake_set.add((0, 0))

direction = 0  
time = 0       


head_r, head_c = 0, 0

while True:
    time += 1  


    nr = head_r + dr[direction]
    nc = head_c + dc[direction]

    
    if not (0 <= nr < n and 0 <= nc < n):
        print(time)
        break

    
    if (nr, nc) in snake_set:
        print(time)
        break

    
    snake.appendleft((nr, nc))
    snake_set.add((nr, nc))

    
    if board[nr][nc] == 0:
    
        tail = snake.pop()
        snake_set.remove(tail)
    else:
    
        board[nr][nc] = 0  

    
    head_r, head_c = nr, nc

    
    if time in turns:
        if turns[time] == 'L':
    
            direction = (direction - 1) % 4
        else:  
    
            direction = (direction + 1) % 4