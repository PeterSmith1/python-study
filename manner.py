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
i = 1
j = 1
while(i < 11):
 j=j*i  #计算10
 i = i+1
print(j)
# 统计素数
i = 2
while (i < 100):
 j = 2
 while (j <= (i / j)):
  if not (i % j): break
  j = j + 1
 if (j > i / j):
  print(i,"是素数")
 i = i + 1