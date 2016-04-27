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

    if data[4]=='IPO上市' or data[4]=="F轮-上市前":
        #print data[4].decode("gbk"),data[1].decode("gbk")
        madeitlist.append(data[1])

    # if any(i in BAT for i in data[6:]) and data[4] in stage:
    #     # print data[4].decode("gbk"),data[1].decode("gbk")
    #     madeitlist.append(data[1])

madeitlist = list(set(madeitlist))#delete mutiples

with open("madeitlist.csv","wb") as file:
    for item in madeitlist:
        # print item.decode("gbk")
        file.write(item+"\n")
file.close()

Madeitinvest={}
for company in madeitlist:
    invests=[]
    reader = csv.reader(open('VCdataHMK.csv', 'rU'))
    for line in reader:
        if line[1]==company and not line[4]=='IPO上市后':
            # print line[1]
            invests.append(line)
    Madeitinvest.update({company:invests})

count=0
with open("madeitinvests.csv", "wb") as f3:
        for company in Madeitinvest:
            for invest in Madeitinvest[company]:
                for fund in invest[6:]:
                    if not fund=="":
                        # print fund
                #     # fundlist.append([invest[0],invest[1],fund])
                        f3.write(invest[0]+","+invest[1]+","+invest[4]+","+fund+'\n')
                        count=count+1
f3.close()
print count
#
# #all invests
# import csv
# comlst=[]
# reader = csv.reader(open('VCdataHMK.csv', 'rU'))
# with open("madeitinvests.csv", "wb") as f4:
#     for data in reader:
#         for fund in data[6:]:
#             if not fund=="":
#                 f4.write(data[0]+","+data[1]+","+data[4]+","+fund+'\n')
# f4.close()
