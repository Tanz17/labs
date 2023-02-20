import math

def task1():
    k = int(input("Введите значение - k: "))


    for m in range(k):
        for n in range(k):
            n = n + 1
            m = m + 1
            a = m**2 - n**2
            b = 2*n*m
            c = m**2 + n**2
            print(f'Ваши значения:\n{m} {n} {a} {b} {c}' )

def task2():
    n = int(input("Введите значение - n: "))
    x = int(input("Введите значение - x: "))

    result = 0
    for i in range(n):
        result = result + math.sin(x**(i+1))
    return result

def task3():
    n = int(input("Введите значение - n: "))
    result = 0
    for i in range(n):
        n = i + 1
        result = result + (2**n/math.factorial(n-1))
    return result

print(task1()) 
print(task2()) 
print(task3()) 
