from queue import Queue

n, k = map(int, input().split())

if n >= k:
    print(n - k)
    exit()

MAX = 100000
time = 0
queue = Queue()
visited = [False for _ in range(100001)]

queue.put((n, time))
visited[n] = True

while not queue.empty():
    cur, t = queue.get()

    if cur == k:
        print(t)
        break

    for new in (cur-1, cur+1, cur*2):
        if 0<= new <= MAX and not visited[new]:
            queue.put((new, t+1))
            visited[new] = True