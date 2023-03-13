#!/usr/bin/python3
#coding=utf-8

#####WHY.2022.4.17.國震中心考題4
#####時間計算函數
#輸入一時間（YYYY-MM-DD HH:SS，如：2020-04-15 20:30）
#回覆該天是星期幾 / 計算出該時刻至今經過幾個太陽日(Julian date)
#不足一日時需用浮點數表示之
#太陽日是以公元前4713年1月1日為原點所經過的日數作為日期記載的方式
#如1995年10月9日的太陽日期為2,450,000


#### input date and time
go = 1
while go == 1:
    try:
        #題目規定要輸入HH:SS，似乎是要求分鐘而不是秒數但代號與月份重疊因此用S
        dt = str(input("輸入一時間，不用秒數（YYYY-MM-DD HH:SS，如2020-04-15 20:30）："))
        ### year/month/day/hour/minute(s)
        from datetime import datetime
        dt_date = dt.split(" ")[0].split("-")
        y = int(dt_date[0])
        m = int(dt_date[1])
        d = int(dt_date[2])
        dt_time = dt.split(" ")[1].split(":")
        h = float(dt_time[0])
        s = float(dt_time[1])
       
        ##ERROR
        #### (1)weekday
        week_day = datetime.date(datetime(year=y, month=m, day=d)).isoweekday()
        week = ["星期","一","二","三","四","五","六","日"]
        print("此日為%s%s" %(week[0],week[week_day]))
        go = 0    
    except ValueError:
        print("輸入日期時刻不存在")
        go = 1


####(2)
####solar day
#題目給的範例似乎是沒有計算到若為100的倍數且不為400的倍數則為平年，為400的倍數則為閏年
#因此假定那個是錯的
def SolarDay(y,m,d,h,s):
    ###判斷此年為平年或閏年(leap=1:閏年)
    if y % 4 == 0: 
        leap = 1
        if y % 100 == 0:
            if y % 400 == 0: leap = 1
            else: leap = 0
    else: leap = 0
    ### 計算公元0年至此年(不包含此年)經過幾個閏年
    leap4   = (y-1) // 4
    leap100 = (y-1) // 100
    leap400 = (y-1) // 400
    ### 計算公元1年1月1日至此日共經過幾天
    month      = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    MonthDays = 0
    ## 若此年為平年
    if leap == 0:
        for i in range(m-1):
            MonthDays += month[i] 
            
    if leap == 1:
        for i in range(m-1):
            MonthDays += month_leap[i]
    days = 365 * (y - 1)  \
         + 1 *(leap4 - leap100 + leap400) \
         + MonthDays \
         + d
    ### 公元前4713年1月1日至公元前1年12月31日共經過幾天
    ## 1潤 5潤 9潤 ...97平 101潤 197潤 297潤 397平 4713潤
    ## +3之後跟公元後一樣算法
    BC = 365 * 4713 + 1 * ((4713+3)//4 - (4713+3)//100 + (4713+3)//400) - 1 
    Solar_Day = days + BC
    ###不足一天的部分
    Solar_Day += (h*60 + s) / (24*60)
    return(Solar_Day)

###該時刻至今經過多少太陽日
##現在
#題目只說是今日，但因為要考慮到不滿一日以浮點計算，因此假設題目指的是此時此秒
today_date = str(datetime.today()).split(" ")[0].split("-")
today_y = int(today_date[0])
today_m = int(today_date[1])
today_d = int(today_date[2])
today_time = str(datetime.today()).split(" ")[1].split(":")
today_h = int(today_time[0])
today_s = int(today_time[1])
print("輸入的日期時刻跟今日此時此刻相差%f個太陽日" \
    %(SolarDay(today_y,today_m,today_d,today_h,today_s)-SolarDay(y,m,d,h,s)))
