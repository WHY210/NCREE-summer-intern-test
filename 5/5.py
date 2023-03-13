#!/usr/bin/python3
#coding=utf-8

####WHY.2022.4.17.國震中心考題5

#試撰寫一網路爬蟲函數，輸入一個關鍵字後回傳第一個google搜尋結果。
#即透過internet 傳送 request 給google 搜尋引擎
#處理google的回傳結果後，將首個超連結回傳。

#reference: https://python-googlesearch.readthedocs.io/en/latest/
from googlesearch import search
query = str(input(""))
print(next(search(query, lang="zh")))

