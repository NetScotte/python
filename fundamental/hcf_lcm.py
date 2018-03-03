# 求最大公倍数，count用于统计次数
def hcf(a, b):
    count = 0
    if a == b:
        return a
    if a < b:
        a, b = b, a
    while True:
        if a % b == 0:
            #            print("计算次数为:".format(count))
            return b
        a, b = b, a % b
        if a < b:
            a, b = b, a
        count += 1


# 求最小公倍数，count表示大数的倍数
def lcm(a, b):
    count = 1
    if b == a:
        return a
    if a < b:
        a, b = b, a
    for num in range(a, a*b+1, a):
        if num % b == 0:
            #print("倍数是{}".format(count))
            return num
        count += 1


'''
#测试用例
while True:
    num1 = int(input("input a value:"))
    num2 = int(input("input other value:"))
    print(hcf(num1, num2))
'''
