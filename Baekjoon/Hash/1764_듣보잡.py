N, M = map(int, input().split())
not_heard = set()
result = []

for _ in range(N):
    not_heard.add(input())
    
for _ in range(M):
    name = input()
    if name in not_heard:
        result.append(name)

result.sort()

print(len(result))
for name in result:
    print(name)