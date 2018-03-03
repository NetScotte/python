a = float(input("输入第一条边:"))
b = float(input("输入第二条边:"))
c = float(input("输入第三条边:"))

s = (a+b+c) / 2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("三角形面积为{}".format(area))
