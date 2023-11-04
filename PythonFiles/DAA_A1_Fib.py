### USE SEPERATE CELLS TO EXWCUTE BOTH METHODS ###

#Method 1 (Use Non-recursion)

nterms =int(input("How many terms? "))
dp = [0]*(nterms+1)
dp[0] = 0
dp[1] = 1
for i in range(2,nterms+1):
  dp[i]=dp[i-1]+dp[i-2]
print("Fibonacci sequence upto", nterms, "th term :")
j=0
while j < len(dp)-1:
    print(dp[j], end=" ")
    j = j + 1

###########################################################################3

#Method 2 (Use Recursion)

def recur_fibo(n):
    if n <= 1:
        return n
    return recur_fibo(n-1) + recur_fibo(n-2)

nterms = int(input("How many terms? "))

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence upto", nterms, "th term :")
    for i in range(nterms):
        print(recur_fibo(i), end=" ")