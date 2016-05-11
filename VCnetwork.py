# -*- coding: gbk -*-
import csv
from datetime import datetime
def cal_top10(bar_time):
    list_inv=[]
    now=datetime.now()
    reader=csv.reader(open("invs.csv", 'rU'))
    for item in reader:
        time=datetime.strptime(item[0],"%Y.%m.%d")
        # bar_time=datetime(2010,5,10)
        if (time-bar_time).days < 0 :
            diff=now-time
            if diff.days<1000:
                wei_days=1.0
            else:
                wei_days=1-round(float(diff.days)/6000,5)*0.5
            list_inv.append([wei_days,item[1],item[2]])


    import networkx as nx
    # print invest_relations
    G=nx.Graph()
    nodes=[]
    for node in list_inv:
        G.add_edge(node[1],node[2],weight=node[0])
        nodes.append(node[1])
        nodes.append(node[2])

    nodes = list(set(nodes))

    Bcdict=nx.betweenness_centrality(G,weight="weight")
    CCdict=nx.closeness_centrality(G)
    EVCdict=nx.eigenvector_centrality(G,weight="weight")
    DegreeDict=nx.degree_centrality(G)
    loaddict=nx.load_centrality(G,weight="weight")

    sCCdict=sorted(CCdict, key=CCdict.__getitem__,reverse=True)
    sCCdict=sCCdict[0:50]
    return sCCdict

    # with open("CentralityCalculationNew-3.csv", "wb") as f2:
    #     f2.write("nodes"+","+"names"+","+"betweenness_centrality"+","+"closeness_centrality"
    #              +","+"eigenvector_centrality"+","+"degree_centrality"+","+"load_centrality"+"\n")
    #     for node in nodes:
    #         # print row
    #         f2.write(str(node)+","+str(Bcdict[node])
    #                  +","+str(CCdict[node])+","+str(EVCdict[node])+","+str(DegreeDict[node])+","+str(loaddict[node])+"\n")
    # f2.close()

with open("centrality10years.csv","wb") as f1:
    for year in range(2000,2017,1):
        bar_time=datetime(year,12,31)
        toplist=cal_top10(bar_time)
        f1.write(str(year)+",")
        print year
        for item in toplist:
            print item.decode("gbk")
            f1.write(str(item)+",")
        f1.write("\n")
f1.close()

