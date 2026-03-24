import sys
sys.setrecursionlimit(2000) # 재귀 한도 확장
input = sys.stdin.readline

n, m = map(int, input().split())

# 1. 그래프 및 방문 리스트 초기화
graph = {i:[] for i in range(1, n + 1)}
visited = {i:False for i in range(1, n + 1)}
count = 0

# 2. 인접 리스트로 그래프 구성 (무방향)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 3. DFS: 연결된 모든 노드를 방문 처리
def dfs(node):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

# 4. 순회하며 방문 안 한 덩어리 찾기
for j in range(1, n + 1):
    if not visited[j]: # 아직 방문 안 했다면 새로운 연결 요소
        count += 1     # 개수 추가
        dfs(j)         # 연결된 노드 전부 방문 처리

print(count)