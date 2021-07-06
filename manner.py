#!/usr/bin/python
# -*- coding: UTF-8 -*-

num1 = 100
num2 = 100.0
num3 = 10000000000
print(num1)
print(num2)
print(num3)


# 选择
a = 21
b = 10
c = 0
if a == b:
 print("a等于b")
else:
 print("a不等于b")
if a > b:
 print("a大于b")
else:
 print("a小于b")
# 运算
sum = a+b
print(sum)

# 循环
number1 = 1
number2 = 1
while(number1 < 11):
 number2=number2*number1  #计算10！
 number1 = number1+1
print(number2)

# 计算素数,循环嵌套
# i = 2
# while (i < 100):
#  j = 2
#  while (j <= (i / j)):
#   if not (i % j):break
#   j = j + 1
#  if (j > i / j):
#   print(i,"是素数")
#  i = i + 1

# python continue语句
for letter in 'python':
 if letter == 'h':
  continue   #continue结束当前一次循环
 print(letter)
# python break语句
for letter1 in 'python':
 if letter1 == 'h':
  break      #break跳出当前循环
 print(letter1)
# pass语句
def sample(number):
 pass #不做任何操作，一般只做占位语句
# 列表
list1 = [1,2,3,4,5]
list2 = ['python','study','java']
print(list1[0])
print(list2[1])

# 元组  与列表的区别是，元祖的元素是无法修改的
tup1 = (1,2,3,4,5)
tup2 = (6,7,8,9,10)
print(tup1)
#虽然元祖不可以修改，但可以通过建立新元祖进行相应的连接组合
tup3 = tup1 + tup2
print(tup3)

# 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
# example: d = {key1 : value1, key2 : value2 }

dict = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(dict['a'])

# 时间与日期
import time
print(time.strftime("%Y-%m-%d %H:%M:%S"),time.localtime())

#python 不定参数，可以处理更多参数。python会自动匹配
# def printinfo(arg1,*vartuple):
#  print(arg1)
#  for var in vartuple:
#   print(var)
# printinfo(10)
# printinfo(10,20,30,40)




