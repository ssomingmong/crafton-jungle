# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(1001)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i:[] for i in range(1, n + 1)}
visited = {i:False for i in graph}
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

for j in range(1, n + 1):
    if not visited[j]:
        count += 1
        dfs(j)

print(count)