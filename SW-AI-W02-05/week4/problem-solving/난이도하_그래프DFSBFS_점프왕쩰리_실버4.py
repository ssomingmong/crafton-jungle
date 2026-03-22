# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    if x >= n or y >= n or visited[x][y]:
        return False
    
    if arr[x][y] == -1:
        return True
    
    visited[x][y] = True
    jump = arr[x][y]

    return dfs(x, y + jump) or dfs(x + jump, y)

if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")