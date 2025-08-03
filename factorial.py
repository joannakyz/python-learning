def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

def factorial_for(n):
    fact = 1
    if n == 0 or n == 1:
        return fact
    else:
        for i in range(1, n + 1):
            fact *= i
        return fact 
    
