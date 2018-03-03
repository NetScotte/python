# 定义装饰器
def myDecorate(func):

    def wrapper(value):
        print('begin wrapper')
        func(value)
        print('end wrapper')

    # 返回一个wrapper函数，等于被装饰函数
    return wrapper

# 使用装饰器
@myDecorate
def myFunc(value):
    print('in myFunc, parameter is:%s'%value)

myFunc(3)
