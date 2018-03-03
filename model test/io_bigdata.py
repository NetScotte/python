
import os
import sys

# 经过大量分析，发现文件为latin1文件格式，对于其他文件格式，请在linux vim下:set fileencoding,并
# 将此程序的latin1改为对应格式
def write_one(source=None,target='../newFile',start_line=0,end_line=100000):
    '''
    将一个大文件中的某些行写入到另一个文件，默认当前目录newFile
    :param source: 数据来源
    :param target: 保存为
    :param start_line: 起始读取行数
    :param end_line: 结束行
    :return: None
    '''

    f2 = open(target, 'w',encoding='utf-8')
    with open(source,'r',encoding='latin1') as f:

        for i,line in enumerate(f):
            if i < start_line:
                continue

            if i >= end_line:
                break

            if (i-start_line)%10000 == 0:
                print('running',(i-start_line)/10000)

            f2.write(line)


def multi_split(source=None,number=5000000):
    '''
    将一个大文件切割成小文件，默认五百万行为一个小文件
    :param source:      数据来源
    :param number:      每number行保存为一个文件
    :return:    None
    '''


    name = '{0}_{1}.txt'
    f2 = open(name.format(source.strip('.txt'),0),'w',encoding='utf-8')

    with open(source,'r',encoding='latin1') as f:
        for i,line in enumerate(f):
            line = line.encode('latin1').decode('utf-8')
            if i%50000 == 0:
                print('running')

            if (i+1)%number == 0:
                path = name.format(source.strip('.txt'), (i+1)/number)
                f2 = open(path,'w',encoding='utf-8')
                print('finish',(i+1)/number)

            f2.write(line)



if __name__ == '__main__':
    # 为变量赋值
    # # 以文件名赋值，需要将程序和文件放在同一个目录
    # source = os.path.join(sys.path[0], 'bigData.txt')
    # target = os.path.join(sys.path[0],'newFile')
    #
    # # 以路径赋值，程序，文件路径任意，注意不能去掉前缀'r'
    # source = r'F:\学习杂件\程序\python\model test\bigData.txt'         # 从该文件读数据
    # # target = r'F:\学习杂件\程序\python\model test\other.txt'       # 写入该文件

    source = r'F:\wiki_new_id_wiki_unique_1944492.txt'
    #
    start = 10000                                                # 起始行数，默认0
    end = 300000                                                 # 终止行数默认10000
    #

    #调用函数
    write_one(source,start_line=start,end_line=end)
    # multi_split(source)

    # 构造大文件，以供测试
    # with open('../bigData.txt','w') as f:
    #     i=0
    #     while(i<100000000):
    #         f.write('该文章实际上提供了集中读取大文件的方式，先经过测试总结如下\n')
    #         i += 1
    #         if i%1000000 == 0:
    #             print('running ',i/1000000)



