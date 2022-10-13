def factorial(num):
    if(num == 1):
        return num
    else:
        temp = factorial(num - 1)
        return num * temp    

res = factorial(5)
print(res)