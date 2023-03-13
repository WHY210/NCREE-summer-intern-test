#!/usr/bin/python3
#coding=utf-8

####WHY.2022.4.17.國震中心考題2

##更改檔案絕對路徑
import os
from numpy import column_stack
path = str(input("存放的資料夾位置 : "))
path = path.replace("\\","/")
#path = "C:/Users/dulci/OneDrive - 國立陽明交通大學/大二/下/GPS/HW1/過程用的檔案"
os.chdir(path)

 ##讀取CSV檔
 #,encoding='utf-8'
import pandas as pd
import csv
f = open('import.csv') 
rows = csv.reader(f)
df = []
for row in rows:
    df.append(row)
f.close()
for r in range(len(df)):
    del df[r][0] #cnty_code
    del df[r][1] #lie
    del df[r][1] #lin
    #合併road,zone,lane or alley
    df[r][1] = df[r][1]  + df[r][2]  + df[r][3] +df[r][4]
    del df[r][2] 
    del df[r][2]
    del df[r][2]
columns = df[0]
columns.append("floor")
columns[1] = "road, zone, lane or alley"
del df[0]
for r in range(len(df)):
    df[r].append("")
    for w in range(len(df[r][2])):
        z.append(w)
        if df[r][2][w] == "號":
            df[r][3] = df[r][2][w+1:]
              
    
        
###生成CSV檔
##輸出整理後的新檔案
export = pd.DataFrame(df, columns = columns)
export 
#print(export)
export.to_csv("export.csv", index=False, encoding='big5')
