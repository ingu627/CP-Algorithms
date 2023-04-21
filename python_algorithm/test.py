from collections import deque

def bfs(graph, start, visited):
     queue = deque([start])
     visited[start] = True
     
     while queue:
         v = queue.popleft()
         print(v, end=' ')
         for i in graph[v]:
             if not visited[i]:
                 queue.append(i)
             visited[i] = True
                 
# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
    [],
    [2, 3, 8], # node 1이 node 2,3,8 과 연결되어 있다.
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)