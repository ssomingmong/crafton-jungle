# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline

computer = int(input())
n = int(input())
graph = {i:[] for i in range(1, computer + 1)}
visited = [False] * (computer + 1)

for _ in range(n):
    u ,v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    count = 0

    for j in graph[node]:
        if not visited[j]:
            count += 1
            count += dfs(j)
    return count

print(dfs(1))