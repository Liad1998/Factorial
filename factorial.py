def Factorial(n):
  ans = 1
  for i in range(2,n+1):
    ans*=i
  return ans
def Prime(n):
  for i in range(2,n):
    if n%i == 0:
      return False
  return True    
