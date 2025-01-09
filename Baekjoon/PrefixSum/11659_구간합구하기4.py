import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0]

for i in range(N):
    sum.append(sum[i] + nums[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])