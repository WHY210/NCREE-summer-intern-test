#!/usr/bin/python3
#coding=utf-8

####WHY.2022.4.17.國震中心考題3
##請將txt檔(HOUF43D10.txt)中的地址部分擷取出來
##計算所有地址用到的字符頻率(數字符號變換為D, 英文符號變換為A，如: B101室 → ADDD室)
##儲存成一個txt檔，並將頻率大於2的字符與其頻率儲存成另一txt檔。

## print當前目錄
##更改檔案絕對路徑
import os
from tkinter import FALSE
path = str(input("請複製存放txt檔的資料夾路徑:"))
path = path.replace("\\","/")
os.chdir(path)


## 讀取txt成list
file = 'HOUF43D10.txt'
f = None
try:
    f = open(file, 'r', encoding='utf-8')
    text = []
    for line in f:
        text.append(line)
    print(text)
    f.close()
except IOError:
    print('ERROR: can not found ' + file)
    if f:
        f.close()
finally:
    if f:
        f.close()

## 找到地址的部分
address = text[23:]

## 轉換字符
new = address
for n in range(len(address)):
    address[n] = address[n][:-1] 
    for w in range(len(address[n])):
        w = 0
        #.isalpha()
        if ord(address[n][w]) in range(65,91) or ord(address[n][w]) in range(97,123):
            if new[n][w] != "A" and new[n][w] != "D":
                new[n] = new[n][1:]
                new[n] += "A"
        elif address[n][w].isdigit() and address[n][w] != "D":
            new[n] = new[n][1:]
            new[n] += "D"
        else:
            new[n] += new[n][w]
            new[n] = new[n][1:]
            
print(new)
##結果輸出
newfile_1 = './output1.txt'
nf1 = open(newfile_1, 'w', encoding='utf-8')
for n in range(len(new)):
    new[n] += "\n"
    nf1.write(new[n])
nf1.close()

##計算英文/數字的頻率，頻率大於2的丟另一個檔
newfile_2 = './output2.txt'
nf2 = open(newfile_2, 'w', encoding='utf-8')
address = text[1:4]
for n in range(len(new)):
    newA = "" 
    newD = ""
    A = 0
    D = 0
    for w in range(len(new[n])):
        if new[n][w] == "A":
            A += 1
        elif new[n][w] == "D":
            D += 1
    if A > 2:
        for i in range(len(new[n])):
            if new[n][i] == "A":
                newA += address[n][i]
        nf2.write("%s (頻率為%d) " %(newA,A))
    if D > 2:
        for j in range(len(new[n])):
            if new[n][j] == "D":
                newD += address[n][j]
        nf2.write("%s (頻率為%d) " %(newD,D))
    nf2.write("\n")
nf2.close()
