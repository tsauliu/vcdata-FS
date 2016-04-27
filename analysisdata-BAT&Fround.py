# -*- coding: gbk -*-
#import data
import csv
reader = csv.reader(open('VCdataHMK.csv', 'rU'))
madeitlist=[]
BAT=["腾讯", "阿里巴巴", "百度", "云锋基金"]
stage=["C轮", "D轮", "E轮"]
# stage=["E轮"]
i=0
for data in reader:
    if data[4]=='IPO上市' or data[4]=="F轮-上市前"\
            or any(i in BAT for i in data[6:]):# and i<2000:
        #print data[4].decode("gbk"),data[1].decode("gbk")
        madeitlist.append(data[1])
    #i=i+1
    if any(i in BAT for i in data[6:]) and data[4] in stage:
        print data[4].decode("gbk"),data[1].decode("gbk")