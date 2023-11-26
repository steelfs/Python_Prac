# x = lambda a, b, c : a + b + c
# print(x(1, 2, 3))

def Func(n):
    return lambda a : a * n

Tripler = Func(3)
doubler = Func(2)

double = doubler(10) # 11 will set into a in lambda
triple = Tripler(10)
print(double)


# def Tri_Recursion(x: int) -> int:
#     if x > 0:
#         result = x + Tri_Recursion(x - 1)
#     else:
#         return 0
#     return result

# z = Tri_Recursion(4)
# print(z)

# def Func(fname):
#   name = f'{fname}_name'
#   print(name)
  
  
# def func(dictionary):
#     for key, value in dictionary.items():
#         print(key, value)

# func({'car': 123})

# def Func(x:int)-> int:
#   return x * 5

# z = Func(8)
# print(z)
