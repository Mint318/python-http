import  sys
print(sys.argv[0])   #代表是绝对路径下的文件
print(sys.argv[1])   #argv[1]代表传递的第一个参数
print(sys.argv[2])
f1 = open("dir.txt","a")
# for line in f1.readlines():
#     print(line.strip())
f1.write('\r\nxzh')
f1.close()
f2=open("dir.txt")
for line in f2.readlines():
    print(line.strip())
f2.close()