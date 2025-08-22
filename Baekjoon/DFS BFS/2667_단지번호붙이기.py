n = int(input())
board = [list(input()) for _ in range(n)]
stack = []
visited = [[False for _ in range(n)] for _ in range(n)]
town = []
dir_r = [0, 0, 1, -1]
dir_c = [1, -1, 0, 0]

def bfs(row, col):
    stack = [(row, col)]
    visited[row][col] = True
    count = 1

    while stack:
        r, c = stack.pop()

        for i in range(4):
            nr = r + dir_r[i]
            nc = c + dir_c[i]

            if nr < 0 or nc < 0 or nr >= n or nc >= n: continue
            if visited[nr][nc] or board[nr][nc] != '1': continue

            visited[nr][nc] = True
            stack.append((nr, nc))
            count += 1

    return count

for r in range(n):
    for c in range(n):
        if visited[r][c] or board[r][c] == '0':
            continue

        town.append(bfs(r, c))

town.sort()
print(len(town))
for t in town:
    print(t)