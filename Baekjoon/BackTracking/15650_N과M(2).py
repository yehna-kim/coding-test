def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for n in combination(arr[i+1:], r-1):
                yield [arr[i]] + n

N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]

for i in combination(numbers, M):
    print(' '.join(map(str, i)))