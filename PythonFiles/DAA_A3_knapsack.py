def knapSack(W, wt, val):
  n = len(val)
  dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
  includedItems = [[False for _ in range(W + 1)] for _ in range(n + 1)]

  for i in range(n + 1):
    dp[i][0] = 0

  for j in range(W + 1):
      dp[0][j] = 0

  for i in range(1,n+1):
    for j in range(1,W+1):
      v = val[i - 1] # ith item val
      w = wt[i - 1] # ith item wt
      if w<=j:
        includedProfit = v + dp[i-1][j-w]
        excludedProfit = dp[i-1][j]
        dp[i][j] = max(includedProfit, excludedProfit)
        if includedProfit>excludedProfit: includedItems[i][j] = True
      else:
        excludedProfit = dp[i-1][j]
        dp[i][j] = excludedProfit
 
  # for i in range(n+1):
  #   for j in range(len(dp[i])):  
  #     print(dp[i][j], end=" ")
  #   print()
  
  # Find the included items
  selected_items = []
  i, j = n, W
  while i > 0 and j > 0:
    if includedItems[i][j]:
      selected_items.append(i)
      j -= wt[i - 1]
    i -= 1

  selected_items.reverse()

  print("Selected items:", selected_items)

  return dp[n][W]


# Driver code

#EX 1
# val = [15, 14, 10, 45, 30 ]
# wt = [2, 5, 1, 3, 4]
# W = 7

#EX 2
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

print(f'Maximum value we can obtain = {knapSack(W, wt, val)}')