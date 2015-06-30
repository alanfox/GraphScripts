# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:54:02 2015

@author: af26

Takes connectivity graphs for several years and combines them into a single 
graph. Two edge weights are given: one is a sum of the weights in the 
years, the other is the number of years when the connection exists.
"""

import networkx as nx

years = range(1990,2001)

H = nx.DiGraph()

for year in years:
    graph_file = ('C:/Users/af26/LarvalDispersalResults/' + 
                    'polcoms' + str(year) + 
                    '/Run_1000_baseline/Networkdata/GraphCompose/' + 
                    'graph_compose.graphml')
    infile = open(graph_file,'r')                
    G = nx.read_graphml(infile)
    infile.close()

    for node in G.nodes():
        H.add_node(node)
        
    for u,v,data in G.edges_iter(data=True):
        w = data['weight']
        if H.has_edge(u,v):
            H[u][v]['weight'] += w
            H[u][v]['nyears'] += 1
        else:
            H.add_edge(u, v, weight=w, nyears = 1)
                    
graph_file = ('C:/Users/af26/LarvalDispersalResults/' + 
                'polcoms1990to2000' +
                '/Run_1000_baseline/Networkdata/GraphCompose/' + 
                'graph_compose.graphml')
outfile = open(graph_file,'w')                
nx.write_graphml(H, outfile)
outfile.close()
