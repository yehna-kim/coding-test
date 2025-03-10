arr1 = input()
arr2 = input()
len1, len2 = len(arr1), len(arr2)

dp = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if arr1[i-1] == arr2[j-1]:
            cur = dp[j-1][i-1] + 1
        else:
            cur = max(dp[j-1][i], dp[j][i-1])
        dp[j][i] = cur

print(dp[len2][len1])