# Practice for today!


def sum(a, b):
    return a + b


lambda a, b: a + b
another_sum = lambda a, b: a + b

print(sum(5,3))

print(another_sum(5,3))

def apply_func(elements, func):
    for element in elements:
        print(func(element))

my_func = lambda x: x * x     # You can change the ending to whatever you want. 
apply_func([1, 2, 3, 4, 5], my_func)











