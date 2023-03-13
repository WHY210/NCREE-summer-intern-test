#!/usr/bin/python3
#coding=utf-8

####WHY.2022.4.17.國震中心考題1

"""
下載人口消長資料 (建議 社會經濟資料服務平台segis)
取得最近20年台灣地區(不計算離島)人口
每年的人口總數/出生總數/死亡總數(三個欄位)
請自行定義CSV格式，儲存以上的答案。CSV檔案名稱請自行命名
利用 matplotlib 繪製(人口總數/出生總數/死亡總數 )折線圖
"""
import pandas as pd
import numpy as np

lst = ["Jay","Raj","Jack"]
df = pd.DataFrame(lst, columns = ['Name'])

import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
motor = pd.read_csv("number of motorcycle.csv")
motor.head(3)    # 顯示前3筆資料
ym = [None] * len(motor["YearMonth"])     # 建立一個空列表，數量為年月的數量

# 以for迴圈逐一將年月資料類別轉成字串類別
for i in range(len(motor["YearMonth"])):  
    ym[i] = str(motor["YearMonth"][i])
    
motor["YearMonth"] = ym  # 將原本年月欄位資料替換掉

plt.style.use("ggplot")               # 使用ggplot主題樣式

#畫第一條線，plt.plot(x, y, c)參數分別為x軸資料、y軸資料及線顏色 = 紅色
plt.plot(motor["YearMonth"], motor["Gas(hundreds of thousands )"],c = "r")  
#畫第二條線，plt.plot(x, y, c)參數分別為x軸資料、y軸資料、線顏色 = 綠色及線型式 = -.
plt.plot(motor["YearMonth"], motor["Electric(thousand)"], "g-.")
#畫第三條線，plt.plot(x, y, c)參數分別為x軸資料、y軸資料、線顏色 = 綠色及線型式 = -.
#plt.plot(motor["YearMonth"], motor["Electric(thousand)"], "b-.")

# 設定圖例，參數為標籤、位置
plt.legend(labels=["Gas motorcycle(hundreds of thousands )	", "Electric motorcycle(thousand)"], loc = 'best')
plt.xlabel("YearMonth", fontweight = "bold")                # 設定x軸標題及粗體
plt.ylabel("Number of motorcylces", fontweight = "bold")    # 設定y軸標題及粗體
plt.title("Motorcycles growth", fontsize = 15, fontweight = "bold", y = 1.1)   # 設定標題、文字大小、粗體及位置
plt.xticks(rotation=45)   # 將x軸數字旋轉45度，避免文字重疊

plt.savefig("Motorcycles growth.jpg",   # 儲存圖檔
            bbox_inches='tight',               # 去除座標軸占用的空間
            pad_inches=0.0)                    # 去除所有白邊
plt.close()      # 關閉圖表