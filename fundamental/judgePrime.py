def is_prime(a):
    if a <= 1:
        return False
    if a == 2:
        return True
    for num in range(2, a):
        if a % num == 0:
            return False
        if num >= a / 2:
            break
    return True

'''
while True :
    try:
        a = int(input("input a value to judge prime:"))
        print(is_prime(a))
    except KeyboardInterrupt :
        print("end")
        break
'''
