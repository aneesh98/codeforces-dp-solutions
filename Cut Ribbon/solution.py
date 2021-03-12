n, a, b, c = [int(num) for num in input().split()]
dp = [x for x in range(n+1)]
dp[0] = 0
for i in range(1, n+1):
    cut1 = max(i-a, -1)
    cut2 = max(i-b, -1)
    cut3 = max(i-c, -1)
    sol1 = -1
    sol2 = -1
    sol3 = -1
    if cut1 >= 0:
        sol1 = dp[i-a]
    if cut2 >= 0:
        sol2 = dp[i-b]
    if cut3 >= 0:
        sol3 = dp[i-c]
    if sol1==-1 and sol2 == -1 and sol3 == -1:
        dp[i] =-1
    else:
        dp[i] = max(sol1, sol2, sol3) + 1
print(dp[n])

        
 