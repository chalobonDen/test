print ("hello world")
x = 5
# บอก data type 
print (type(x)) 

#แปลง data type
y = float(x)
print (type(y)) 
print (y)

data = [1, 2, 3, 4]
#ถามขนาดของ list 
#len(data) บอกขนาดของlist
c = data.pop(0)
print(c)
print (len(data))
#4

a = [1, 2, 3]
b = a[:]
b[0] = 100
print(a)
print(b)

# การใช้ string แบบ """ เว้นบรรทัดตามข้อความที่พิมพ์เลย
content = """ 
    this is jayjay
    i am 23 years old
    """
print (content)

# การต่อstring ใช้ + ได้กับ string + string เท่านั้น *ถ้าเป็นข้อมูลชนิดอื่นต้องทำการแปลงเป็น string ก่อน
name = "Jihoon"
lastname = "Park"
year = 1999
print(lastname+" "+name+" "+str(year))

# สามารถใช้ * กับ string ได้
strmul = "nong jihoon is so cute.\n"*3
print (strmul)