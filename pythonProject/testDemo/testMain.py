# coding = utf8
"""
s1 = "a a a bb"
s2 = "aaab"
ss1 = s1.split(" ")
print(ss1)
print(ss1[0])
x = 11
y = 22
print(len(s1))
print( x <= y )
print( s1 > s2 )
print( s1.__contains__( s2 ) )

d = 1
while d < 8:
    if d < 6:
        print( "星期" + str( d ) + "上班" )
    else:
        print( "星期" + str( d ) + "休息" )
    d += 1



for j in range(1,10):
    for z in range(1,10):
        if(z<=j):
            s = j*z
            print(str(z)+"*"+str(j)+"="+str(s)+"  ",end="")
    print()

print("===========================")
list1 = [1,2,3,4,5,6]
for ii in range(len(list1)):
    print(list1[ii])

index = 0
while index<len(list1):
    print(list1[index])
    index+=1

str = 'hello world,{name}'
str1 = "hello,{names},i am {age},my hobby is {hobby}"
str2 = "helloworld111"
print("我叫%s，今年%d岁"%("小明",10))
print(str.capitalize())
print(str.count('o'))
print(str.count('o',4,6))
print(str.endswith('ld'))
print(str.endswith('o',1,5))
print(str.find('world'))
print(str.format(name = 'xiaoming'))
print(str1.format_map({"names":"xiaohong","age":10,"hobby":"pingpong"}))
print(str.isalnum())
print(str2.isalnum())
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import glob
import os
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')

    def bar(self,message):
        print ("%s from Parent" % message)

class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild,self).__init__()
        print ('Child')

    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

list = [1,2,3,4,5]
it = iter(list)
for i in it:
    print(i,end=",")
    print()
fi = open("text.txt","w+")
print(fi.name)
print(fi.mode)
print(fi.tell())
fi.close()

#add comment
if os.path.isfile("C:\\test\\test111.txt"):
    print("file exists")
    output = open("C:\\test\\test111.txt","r+")
    content = output.read(10)
    print(content)
    print(output.tell())
    output.close()
else:
    print("file not exists")
    input = open("C:\\test\\test111.txt","w+")
    input.write("write something")
    input.close()