# -*- coding: gbk -*-
import csv
from datetime import datetime
list_inv=[]
now=datetime.now()
reader=csv.reader(open("invs.csv", 'rU'))
for item in reader:
    time=datetime.strptime(item[0],"%Y.%m.%d")
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
# print Bcdict
# print CCdict
# print EVCdict
# print nodes

with open("CentralityCalculationNew-2.csv", "wb") as f2:
    f2.write("nodes"+","+"names"+","+"betweenness_centrality"+","+"closeness_centrality"
             +","+"eigenvector_centrality"+","+"degree_centrality"+","+"load_centrality"+"\n")
    for node in nodes:
        # print row
        f2.write(str(node)+","+str(Bcdict[node])
                 +","+str(CCdict[node])+","+str(EVCdict[node])+","+str(DegreeDict[node])+","+str(loaddict[node])+"\n")
f2.close()