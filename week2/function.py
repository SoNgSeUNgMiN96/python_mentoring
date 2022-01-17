def add(a,b):
    return a + b

def sumUp(n,sum):
    if n==0:
        return sum
    return sumUp(n-1,sum+n)

def factorial(n,sum):
    if n==0:
        return sum
    return factorial(n - 1, sum*n)


print(add(1,2))
print(sumUp(10,0))  # 1에서 N 까지의 수를 재귀적으로 더해준다.
print(factorial(10,1))  # 1에서 N 까지의 수를 재귀적으로 곱해준다.
