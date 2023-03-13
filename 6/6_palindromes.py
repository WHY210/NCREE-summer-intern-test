#!/usr/bin/python3
#coding=utf-8

####WHY.2022.4.17.國震中心考題6
####迴文數 (Palindromes)
###輸入2位數以上的任意正整數n，和它逆序翻轉後形成的新數相加
###如此循環下去，要加幾次才會得到迴文數?
###若超過5000次還無法得到迴文數，則輸出"no"。

## input number (2 digits) as n
go = 1
while go == 1:
  try:
    n = int(input("輸入2位數以上的任意正整數："))
    if n < 10:   
      assert False
    go = 0
  except AssertionError:
    print("數字過小，請重新輸入")
    go = 1
  except ValueError:    
    print("非數字，請重新輸入")
    go = 1
  
## reverse function
def reverse(num):
  num = str(num)[::-1]
  return num

## plus reversed number function
def plus(num):
  re_num = reverse(num)
  sum = int(num) + int(re_num)
  return str(sum)

## run
k = 1
while k in range(1,5000):
  n = plus(n)
  if n == reverse(n):
    print("加了%s次得到迴文數%s" %(k,n))
    break
  else: 
    k += 1
if n != reverse(n):
  print("no")