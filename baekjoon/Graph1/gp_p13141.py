import sys
input = sys.stdin.readline

N,M = map(int,input().split())

DP = [[1e9]*N for i in range(N)]
graph = []
for _ in range(M):
  a,b,c = map(int,input().split())
  DP[a-1][b-1] = DP[b-1][a-1] = min(DP[a-1][b-1],c)
  graph.append((a-1,b-1,c))

for k in range(N):
  for i in range(N):
    for j in range(N):
      DP[i][j] = min(DP[i][j],DP[i][k]+DP[k][j])
for i in range(N):
  DP[i][i] = 0
result = 1e9
for i in range(N):
  MAX = 0
  for a,b,c in graph:
    MAX = max(MAX,(DP[i][a]+c+DP[b][i])/2)
  result = min(result,MAX)
print(result)