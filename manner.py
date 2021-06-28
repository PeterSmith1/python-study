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

# 计算素数
i = 2
while (i < 100):
 j = 2
 while (j <= (i / j)):
  if not (i % j):break
  j = j + 1
 if (j > i / j):
  print(i,"是素数")
 i = i + 1