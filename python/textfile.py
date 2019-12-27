def write_demo():
    f = open('D:/test/python/demo.txt', 'w')
    f.write("hello world")
    f.close()

write_demo()


def read_demo():
    f = open('D:/test/python/myconfig.txt', 'r') #ต้องใส่ path ให้ครบ
    s = f.read()
    print(s)
    f.close()

read_demo()

