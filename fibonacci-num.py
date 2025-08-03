def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#faster version of fibonacci numbers
  def fibonacci(n):
    fib = [0 , 1]
    for i in range(2, n+1):
      fib.append(fib[i-1] + fib[i - 2])
    return fib[n]
