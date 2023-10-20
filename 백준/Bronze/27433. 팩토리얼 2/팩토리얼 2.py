def factorial(n:int)->int:
    if n == 0 or n == 1:
        return 1
    a = 1
    while n:
        a *= n
        n -= 1
    return a
    
print(factorial(int(input())))