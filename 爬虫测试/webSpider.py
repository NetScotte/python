from urllib.request import urlopen

# if __name__ == '__main__':
#     m = urlopen("http://www.baidu.com").read()
#     with open("./1.html", "wb") as f:
#         f.write(m)
#     f.close()

f = open("./1.html", "wb")
res = urlopen("http://www.runoob.com/python3/python3-inputoutput.html")
for line in res:
    line = line.decode("utf-8")
    f.write(line)

f.close()
