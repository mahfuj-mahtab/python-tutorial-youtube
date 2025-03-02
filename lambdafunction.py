# def sum(a,b):
#     return a + b

# print(sum(10,20))

# add = lambda a,b :  a+b

# print(add(10,20))

# square = lambda a : a**2

# print(square(5))

def multiplier(x):
    return lambda a : x * a

result1 = multiplier(10)
print(result1(5))
def a(a,b):
    return a * b
print(a(10,5))