def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,11):
    print(i, fibonacci(i))

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print()
for i in range(1,11):
    print(i, factorial(i))

def pascal(n):
    if n==1:
        return [1]
    else:
        past = pascal(n-1)
        future = [1]
        for i in range(n-2):
            future.append(past[i]+past[i+1])
        future.append(1)
        return future

print()
for i in range(1,11):
    print(i, pascal(i))

