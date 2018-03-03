a = float(input('input a : '))
b = float(input('input b : '))
print(f"before switch , a is {a} b is {b}")
a, b = b, a
print(f"after switch , a is {a} b is {b}")
