from collections import deque

T = int(input())

for _ in range(T):
    cmd = list(input().replace('RR', ''))
    n = int(input())
    if n <= 0: arr = deque(input()[1:-1])
    else: arr = deque(list(map(int, input()[1:-1].split(','))))
    reverse = False
    
    if n < cmd.count('D'):
        print('error')
        continue

    for f in cmd:
        if f == 'R':
            reverse = False if reverse else True

        elif f == 'D':
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if not reverse:
        print(str(list(arr)).replace(' ', ''))
    else:
        arr.reverse()
        print(str(list(arr)).replace(' ', ''))