node = int(input())
edge = int(input())
graph = []
stack = []
visited = [False for _ in range(node + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph.append((a, b))
    graph.append((b, a))
    
visited[1] = True
stack.append(1)

while stack:
    node = stack.pop()
    
    for s, e in graph:
        if s == node and not visited[e]:
            visited[e] = True
            stack.append(e)
    
            
result = visited.count(True)
print(result - 1)