'''
# 可以通过sys._getframe().f_locals查看以下名字空间
# 遵循LEGB
# locals函数内的名字空间，包括局部变量和形参
# enclosing外部嵌套函数的名字空间，（闭包中常见，如上例a)
# globals全局变量，函数定义所在模块的名字空间
# builtins内置模块的名字空间
'''
a=3
def f():
    a=4
    def v():
        print(a)
    return v
test=f()
test()




'''
导入顺序：
1.先在当前脚本目录里寻找有没有与导入模块名称相同的文件，不应该与内置变量等重名
2.查找模块路径下有没有对应的模块名

工作方式：
找到模块
编译成字节码文件，如果有则导入字节码文件
执行其中的代码
以上只有在模块被第一次导入时才运行，否则会直接提取内存中的模块
在模块中，所有以_开头的都不会被from *导入，只会导入__all__列表里面的变量
import sys
for n in sys.path:
    print(n)

# 最后一个目录就是内置模块路径
# 重新导入某个函数
import imp
imp.reload(func)
'''
