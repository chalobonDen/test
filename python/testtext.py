f = open('D:/test/python/myconfig.txt', 'r')

while True:
    s = f.readline()

    if s == '': # check file end
        break

    # spliting line to key and value
    d = s.rstrip().split('=')
    print(d[0] + ': ' + d[1])

f.close()
