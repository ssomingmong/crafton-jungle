# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import deque
import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, n + 1):
    graph[i].sort()


def dfs(start):
    visited = [False] * (n + 1)
    result = []

    def recurse(node):
        visited[node] = True
        result.append(node)

        for nxt in graph[node]:
            if not visited[nxt]:
                recurse(nxt)

    recurse(start)
    return result

def bfs(start):
    visited = [False] * (n + 1)
    result = []
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        result.append(node)

        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    return result


print(*dfs(v))
print(*bfs(v))