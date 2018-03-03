#将一个英文文本文件分词，统计单词和词频，并排序，之后可以单独使用关键词和词频
# with open("./test.txt") as f:
#     key={}
#     for line in f:
#         tokens = line.split()
#         for string in tokens:
#             if string in key:
#                 key[string] += 1
#             else:
#                 key[string] = 1
#     sortedKey = sorted(key.items(), key=lambda e: e[1],reverse=True)
#     print(sortedKey)
#     print(sortedKey[1][0])
#
# def keyWord(type):
#     key = {}
#     for i in range(1, 3):
#         with open("{0}{1}.txt".format(type, i), encoding='gbk') as f:
#             for line in f:
#                 tokens = line.split()
#                 for string in tokens:
#                     if string in key:
#                         key[string] += 1
#                     else:
#                         key[string] = 1
#     sortedkey = sorted(key.items(), key=lambda a: a[1], reverse=True)
#     print(sortedkey)
#
# keyWord("test")