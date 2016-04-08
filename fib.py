arr = {}
arr[0] = 1
arr[1] = 1
def nthFib(n):
  if (n == 0) or (n == 1):
    return 1
  if (n-1 not in arr):
    arr[n-1] = nthFib(n-1)
  if (n-2 not in arr):
    arr[n-2] = nthFib(n-2)
  arr[n] = arr[n-1] + arr[n-2]
  return arr[n]

print(nthFib(6))

