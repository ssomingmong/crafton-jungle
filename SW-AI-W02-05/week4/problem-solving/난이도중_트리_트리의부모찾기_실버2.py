# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725


n = int(input())

graph = {i:[] for i in range(1, n + 1)}
visited = {i:False for i in range(1, n + 1)}
parent = [0] * (n + 1)

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            parent[nxt] = node
            dfs(nxt)

dfs(1)
for j in range(2, n + 1):
    print(parent[j])