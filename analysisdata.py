# -*- coding: gbk -*-
#import data
import csv
reader = csv.reader(open('VCdataHMK.csv', 'rU'))

#get the list of IPO companys
i=0
IPOcompanys=[]
for data in reader:
    if i<10:
        print data
    if data[4]=='IPO上市':
        print "shit"
        # print data[4].decode('gbk')
        IPOcompanys.append(data[1])
    i=i+1
print i
#get the list of made-it VC who invest in those companys
for cpys in IPOcompanys:
    print cpys.decode("gbk")

IPOinvest={}
for company in IPOcompanys:
    invests=[]
    reader = csv.reader(open('VCdataHMK.csv', 'rU'))
    for line in reader:
        if line[1]==company and not line[4]=='IPO上市后':
            # print line[1]
            invests.append(line)
    IPOinvest.update({company:invests})
# print IPOinvest

fundlist=[]
with open("shangshi_data.csv", "wb") as f2:
    with open("fundipo_data.csv", "wb") as f3:
        for company in IPOcompanys:
            # f2.write(company+","+"\n")
            for invest in IPOinvest[company]:
                if not invest[4]=="IPO上市":
                    for shit in invest:
                        f2.write(shit+",")
                    # f2.write('\n')
                for fund in invest[6:]:
                    if not fund=="":
                        # print fund
                #     # fundlist.append([invest[0],invest[1],fund])
                        f3.write(invest[0]+","+invest[1]+","+invest[4]+","+fund+'\n')
                f2.write('\n')
            f2.write('\n')
    f3.close()
f2.close()

# for fundlistitem in fundlist:
#     print fundlistitem


